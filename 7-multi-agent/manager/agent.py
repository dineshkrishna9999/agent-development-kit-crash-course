from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv
load_dotenv()

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst
from .sub_agents.greeting_agent.agent import greeting_agent
from .tools.tools import get_current_time

root_agent = Agent(
    name="manager",
    model=LiteLlm(model=os.environ["AZURE_MODEL"]),  #or model = "gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd
    - greeting_agent

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    sub_agents=[stock_analyst, funny_nerd, greeting_agent],
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)
