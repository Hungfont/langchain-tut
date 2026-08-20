
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """Search for information based on a query."""
    print(f"Searching for: {query}")
    return tavily.search(query)


llm = ChatDeepSeek(
    model="deepseek-chat",
)

tools = [search]
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
