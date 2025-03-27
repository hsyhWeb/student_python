import io
from flask import Flask, send_file, request
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pymysql
import matplotlib

pymysql.install_as_MySQLdb()

# 配置中文显示和负号问题
matplotlib.rcParams.update({
    'font.sans-serif': ['SimHei'],
    'axes.unicode_minus': False
})

# 创建数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/student_scores?charset=utf8')
work_conn_read = engine.connect()

app = Flask(__name__)

def generate_total_score_bar(student_name):
    sql = f"""
        SELECT `考试名称`, `总分` 
        FROM scores 
        WHERE `姓名`='{student_name}' 
        ORDER BY `考试名称`
    """
    # engine = create_engine('mysql+pymysql://root:123456@localhost:3306/student_scores?charset=utf8')
    # with engine.connect() as conn:
    #     df = pd.read_sql(sql, con=conn)

    df = pd.read_sql(sql, con=engine)

    plt.figure(figsize=(8, 4))
    plt.bar(df['考试名称'], df['总分'], color='skyblue')
    plt.xlabel('考试名称')
    plt.ylabel('总分')
    plt.title(f'{student_name} 每次考试总分变化趋势')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf

def generate_subject_rank_lines(student_name):
    sql = f"""
        SELECT `考试名称`, `语文级名`, `数学级名`, `英语级名`
        FROM scores
        WHERE `姓名` = '{student_name}'
        ORDER BY `考试名称`
    """
    df = pd.read_sql(sql, con=engine)
    # engine = create_engine('mysql+pymysql://root:123456@localhost:3306/student_scores?charset=utf8')
    # with engine.connect() as conn:
    #     df = pd.read_sql(sql, con=conn)
    plt.figure(figsize=(8, 4))
    plt.plot(df['考试名称'], df['语文级名'], marker='o', label='语文级名')
    plt.plot(df['考试名称'], df['数学级名'], marker='o', label='数学级名')
    plt.plot(df['考试名称'], df['英语级名'], marker='o', label='英语级名')
    plt.xlabel('考试名称')
    plt.ylabel('级名')
    plt.title(f'{student_name} 各科级名变化趋势')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf

@app.route('/visualize/total_score', methods=['GET'])
def visualize_total_score():
    student_name = request.args.get('student_name')
    if not student_name:
        return "缺少参数 student_name", 400
    img_buf = generate_total_score_bar(student_name)
    return send_file(img_buf, mimetype='image/png')

@app.route('/visualize/subject_rank', methods=['GET'])
def visualize_subject_rank():
    student_name = request.args.get('student_name')
    if not student_name:
        return "缺少参数 student_name", 400
    img_buf = generate_subject_rank_lines(student_name)
    return send_file(img_buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
