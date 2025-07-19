import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from quiz_agent import root_agent

load_dotenv()


# Create a new session service to store state
session_service_stateful = InMemorySessionService()

# Simple initial state (just to avoid KeyError)
initial_state = {
    "user_name": "Dinesh",
    "user_preferences": "I want to learn the Google ADK. My favorite programming language is python.",
}

# Create a NEW session
APP_NAME = "quiz_app"
USER_ID = "dineshkrishna9999"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

new_message = types.Content(
    role="user", parts=[types.Part(text="What is the dinesh trying to learn?")],
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("Session completed successfully!")

