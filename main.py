
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch


load_dotenv()


llm = ChatDeepSeek(
    model="deepseek-chat",
)

tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)
def main():
    result = agent.invoke({
    "messages": [
        HumanMessage(content="What is the capital of France?")
    ]
})
    print(result)

if __name__ == "__main__":
    main()
