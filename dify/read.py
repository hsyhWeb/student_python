from flask import Flask, request, jsonify
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

app = Flask(__name__)

# 1. 配置数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/student_scores?charset=utf8')

@app.route('/upload', methods=['POST'])
def upload_excel():
    """
    接收上传的 Excel 文件，并将内容写入数据库
    """
    # 从表单中获取文件对象
    file = request.files.get('file')
    if not file:
        return jsonify({"code": 400, "message": "未检测到文件，请使用 'file' 字段上传 Excel 文件"}), 400

    try:
        # 2. 读取Excel第一行，用于获取考试名称
        df_title = pd.read_excel(file, header=None, nrows=1)
        exam_name = df_title.iloc[0, 0]

        # 注意：读完第一遍后，需要重置文件指针，再读一次
        file.seek(0)

        # 3. 读取正式数据，从第2行开始
        df = pd.read_excel(file, header=0, skiprows=1)

        # 4. 给df增加“考试名称”列
        df['考试名称'] = exam_name

        # 5. 重命名列（根据你实际的列名来）
        df.rename(columns={
            "级名.1": "语文级名",
            "级名.2": "数学级名",
            "级名.3": "英语级名",
            "级名.4": "物理级名",
            "级名.5": "化学级名",
            "级名.6": "生物级名",
            # 如果还有其它重复列需要改名，继续写在这里
        }, inplace=True)

        # 6. 写入数据库
        df.to_sql("scores", con=engine, if_exists='append', index=False)

        return jsonify({"code": 200, "message": "上传并写入数据库成功！"}), 200

    except Exception as e:
        return jsonify({"code": 500, "message": f"服务器异常: {e}"}), 500


if __name__ == '__main__':
    # 7. 运行Flask应用
    app.run(host='0.0.0.0', port=5000, debug=True)
