from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv
load_dotenv()

def get_greeting(name: str) -> dict:
    """Get a greeting for the user."""
    return {
        "greeting": f"Hello {name}! How can I help you today?"
    }

greeting_agent = Agent(
    name="greeting_agent",
    model=LiteLlm(model=os.environ["AZURE_MODEL"]),  #or model = "gemini-2.0-flash",
    description="A greeting agent",
    instruction="""
    You are a helpful assistant that can greet the user and ask them about their name.
    available tools:
    - get_greeting: to get a greeting for the user

    if the user is not able to provide their name, ask them to provide their name.
    use the get_greeting tool to get a greeting for the user.

    if the user asks about anything else, delegate the task to the manager agent.
    """,
    tools=[get_greeting],
)