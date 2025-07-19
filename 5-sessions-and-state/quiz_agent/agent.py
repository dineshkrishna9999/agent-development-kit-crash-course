from google.adk.agents import Agent
import os
from google.adk.models.lite_llm import LiteLlm

from dotenv import load_dotenv
load_dotenv()


# Create the root agent
root_agent = Agent(
    name="quiz_agent",
    model=LiteLlm(model=os.environ["AZURE_MODEL"]),
    description="quiz agent that asks questions to user and provides answers if user is not able to answer",
    instruction="""
    You are a helpful assistant that asks the questions to user based on the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
)
