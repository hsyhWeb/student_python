
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools import tools
from langchain_core.messages import HumanMessage

model = ChatOpenAI(
    base_url="https://api.deepseek.com",
    api_key="sk-3abc0cde989141289a3a4d73a1d965f5",
    model="deepseek-chat",
)
agent_executor = create_react_agent(model, tools)

# if __name__ == '__main__':
#     file_path = "D:\\project\\pycharmProject\\studentScore\\xls\\temp.xlsx"
#     upload_excel(file_path)
