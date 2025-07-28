from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv
from .tools import get_weather

load_dotenv()

root_agent = Agent(
    name="weather_agent",
    model=LiteLlm(model=os.environ.get("AZURE_MODEL")),
    description="A simple weather agent that provides current weather information for major cities",
    instruction="""
    You are a simple weather assistant. Use the get_weather tool when users ask about weather.
    
    Available cities: Chennai,New York, London, Tokyo, Paris, Sydney
    
    Just use the tool and return what it gives you. Be helpful and friendly.
    """,
    tools=[get_weather],
) 