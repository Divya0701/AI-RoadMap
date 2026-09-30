from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import  DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

###Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    description="An agent that can search the web for information using DuckDuckGo.",
    model=Groq(id="openai/gpt-oss-120b",max_tokens=400),
    tools=[DuckDuckGo()],
    instructions=["always include sources when providing information"],
    show_tool_calls=True,
    markdown=True
)

## Financial Agent
financial_agent = Agent(
    name="Financial Agent",
    description="An agent that can provide financial information and analysis using YFinance.",
    model=Groq(id="openai/gpt-oss-120b",max_tokens=400),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["always include sources when providing information"],
    show_tool_calls=True,
    markdown=True
)


##multi agent that combines both the web search agent and the financial agent
multi_ai_agent = Agent(
    team = [web_search_agent, financial_agent],
    name="Multi AI Agent",
    description="An agent that can provide financial information and analysis using YFinance and search the web for information using DuckDuckGo.",
    model=Groq(id="openai/gpt-oss-120b",max_tokens=400),
    instructions=["always include sources when providing information","use tables when providing financial information"],
    show_tool_calls=True,
    markdown=True
)
multi_ai_agent.print_response("Summarize latest information and share the latest news for NVDA",stream=True)
financial_agent.print_response(
    "Give me the current stock price, fundamentals and latest news for NVDA.",
    stream=True
)