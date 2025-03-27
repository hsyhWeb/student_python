from langchain_core.tools import tool
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
import common
from sqlalchemy import create_engine

from common import file_path as path

matplotlib.rcParams.update({
    'font.sans-serif': ['SimHei'],
    'axes.unicode_minus': False
})
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/student_scores?charset=utf8')
file_path = path
@tool
def upload_excel():
    """
    读取 Excel 文件，并将内容写入数据库
    file_path为文件路径
    """
    try:
        file_path = common.file_path
        # 2. 读取Excel第一行，用于获取考试名称
        df_title = pd.read_excel(file_path, header=None, nrows=1)
        exam_name = df_title.iloc[0, 0]

        # 3. 读取正式数据，从第2行开始
        df = pd.read_excel(file_path, header=0, skiprows=1)

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

        return "上传并写入数据库成功！"

    except Exception as e:
        print(f"发生错误: {e}")

@tool
def generate_total_score_bar(student_name):
    """ 根据学生名查询学生的几次考试的总分变化并可视化，并将生成的图片保存在项目目录的 'images' 文件夹中,并返回路径，路径前后换行,注意路径前后后不要有任何字符"""
    sql = f"""
        SELECT `考试名称`, `总分` 
        FROM scores 
        WHERE `姓名`='{student_name}' 
        ORDER BY `考试名称`
    """

    df = pd.read_sql(sql, con=engine)

    plt.figure(figsize=(8, 4))
    plt.bar(df['考试名称'], df['总分'], color='skyblue')
    plt.xlabel('考试名称')
    plt.ylabel('总分')
    plt.title(f'{student_name} 每次考试总分变化趋势')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # 确保 'images' 目录存在
    image_dir = "images"
    os.makedirs(image_dir, exist_ok=True)

    # 生成文件路径
    image_path = os.path.join(image_dir, f"{student_name}_总分可视化.png")

    # 保存图片
    plt.savefig(image_path, format='png')
    plt.close()
    return "http://127.0.0.1:5002//"+image_path  # 返回图片的存储路径


@tool
def generate_subject_rank_lines(student_name):
    # """ 根据学生名生成单科成绩，返回可视化图片路径 """
    """ 根据学生名查询学生的几次考试的单科成绩变化并可视化，并将生成的图片保存在项目目录的 'images' 文件夹中 ，并返回路径 ，路径前后换行,注意路径前后后不要有任何字符"""
    sql = f"""
        SELECT `考试名称`, `语文级名`, `数学级名`, `英语级名`
        FROM scores
        WHERE `姓名` = '{student_name}'
        ORDER BY `考试名称`
    """
    df = pd.read_sql(sql, con=engine)

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

    # 确保 'images' 目录存在
    image_dir = "images"
    os.makedirs(image_dir, exist_ok=True)

    # 生成文件路径
    image_path = os.path.join(image_dir, f"{student_name}_单科级名可视化.png")

    # 保存图片
    plt.savefig(image_path, format='png')
    plt.close()
    return "http://127.0.0.1:5002//"+image_path



tools = [upload_excel,generate_subject_rank_lines,generate_total_score_bar]