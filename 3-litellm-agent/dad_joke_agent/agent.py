import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os 
from dotenv import load_dotenv

load_dotenv()


def get_dad_joke():
    jokes = [
        "what do call a chicken mom ? Chinken keema!",
        "What do you call a chicken father? chicken kebab!",
        "Why did the chicken cross the road? To get to the other side!",
        "What do you call a belt made of watches? A waist of time.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]
    return random.choice(jokes)


root_agent = Agent(
    name="dad_joke_agent",
    model=LiteLlm(model=os.environ["AZURE_MODEL"]),
    description="Dad joke agent",
    instruction="""
    You are a helpful assistant that can tell dad jokes. 
    Only use the tool `get_dad_joke` to tell jokes.
    """,
    tools=[get_dad_joke],
)
