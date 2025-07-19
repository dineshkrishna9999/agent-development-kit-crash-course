# Sessions and State Management in ADK

This example demonstrates how to create and manage stateful sessions in the Agent Development Kit (ADK), enabling your agents to maintain context and remember user information across interactions.

**Modified for learning**: This example has been customized with personalized user data and a quiz agent for interactive learning.

## What Are Sessions in ADK?

Sessions in ADK provide a way to:

1. **Maintain State**: Store and access user data, preferences, and other information between interactions
2. **Track Conversation History**: Automatically record and retrieve message history
3. **Personalize Responses**: Use stored information to create more contextual and personalized agent experiences

Unlike simple conversational agents that forget previous interactions, stateful agents can build relationships with users over time by remembering important details and preferences.

## Example Overview

This directory contains a basic stateful session example that demonstrates:

- Creating a session with user preferences
- Using template variables to access session state in agent instructions
- Running the agent with a session to maintain context

The example uses a quiz agent that creates personalized quizzes based on stored user information in the session state.

## Project Structure

```
5-sessions-and-state/
│
├── basic_stateful_session.py      # Main example script
│
└── quiz_agent/                    # Agent implementation
    ├── __init__.py
    └── agent.py                   # Quiz agent with template variables
```

## Getting Started

### Setup

1. Activate the virtual environment from the root directory:
```bash
# macOS/Linux:
source ../.venv/bin/activate
# Windows CMD:
..\.venv\Scripts\activate.bat
# Windows PowerShell:
..\.venv\Scripts\Activate.ps1
```

2. Create a `.env` file and add your API key:
```
AZURE_MODEL=your_model_here
```

### Running the Example

Run the example to see a stateful session in action:

```bash
python basic_stateful_session.py
```

This will:
1. Create a new session with user information
2. Initialize the quiz agent with access to that session
3. Process a user query about learning preferences
4. Display the agent's response based on the session data

## Key Components

### Session Service

The example uses the `InMemorySessionService` which stores sessions in memory:

```python
session_service = InMemorySessionService()
```

### Initial State

Sessions are created with an initial state containing user information:

```python
initial_state = {
    "user_name": "Dinesh",
    "user_preferences": "I want to learn the Google ADK. My favorite programming language is python.",
}
```

### Creating a Session

The example creates a session with a unique identifier:

```python
stateful_session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
```

### Accessing State in Agent Instructions

The quiz agent accesses session state using template variables in its instructions:

```python
instruction="""
You are a helpful quiz assistant that asks questions to users based on their preferences.

Here is some information about the user:
Name: {user_name}
Preferences: {user_preferences}

IMPORTANT BEHAVIOR:
- If the user's name is "Unknown User" or empty, ask for their real name first
- If preferences say something like "Please tell me what you'd like to learn about", ask them to specify their learning interests
- Once you have real user information, create personalized quizzes based on their stated preferences
"""
```

### Running with Sessions

Sessions are integrated with the `Runner` to maintain state between interactions:

```python
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)
```

### Web Interface

You can also run the quiz agent through the web interface:

```bash
adk web
```

Then select "quiz_agent" from the dropdown. The web interface will start with empty sessions, and the agent will ask for user information during the conversation.

## Additional Resources

- [Google ADK Sessions Documentation](https://google.github.io/adk-docs/sessions/session/)
- [State Management in ADK](https://google.github.io/adk-docs/sessions/state/)
