import os
from flask_cors import CORS
from flask import Flask, request, jsonify, send_file, send_from_directory
from langchain_core.messages import HumanMessage
from werkzeug.utils import secure_filename
import common  # 引入 common.py 作为全局存储
from agent import agent_executor
app = Flask(__name__)
CORS(
    app,
    origins=["http://localhost:5173"],  # 必须明确指定来源，不能用 "*"
    supports_credentials=True           # 允许携带凭据（如 Cookies）
)
# 设置文件存储路径
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'xls')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # 确保文件夹存在

@app.route('/upload_message', methods=['POST'])
def upload_message():
    """
    接收可选的文件(file)和文本消息(message)。
    如果 file 存在，则存储文件到 xls 目录，并更新 common.py 变量。
    """
    file = request.files.get('file')  # 获取上传的文件
    message = request.form.get('message')  # 获取文本消息

    if message:
        common.update_values(common.file_path, message)  # 更新 message_text 变量

    if file:
        filename = secure_filename(file.filename)  # 确保文件名安全
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(save_path)  # 保存文件
        common.update_values(save_path, common.message_text)  # 更新全局 file_path 变量

    response = agent_executor.invoke(
        {"messages": [HumanMessage(content=message)]}
    )

    # 只获取最后一条消息的 content
    last_message = response["messages"][-1].content

    # 构造返回数据
    response_data = {"message": last_message}

    # 如果 common.image_path 存在，添加到返回数据中


    print(response["messages"])
    return jsonify(response_data)
@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)