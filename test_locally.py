import os
from dotenv import load_dotenv
from agent import root_agent
from vertexai.preview import reasoning_engines

load_dotenv()

TEST_USER_ID = os.getenv("TEST_USER_ID")
TEST_MESSAGE = os.getenv("TEST_MESSAGE")

app = reasoning_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

session = app.create_session(user_id=TEST_USER_ID)
print(session)

print(app.list_sessions(user_id=TEST_USER_ID))


for event in app.stream_query(
    user_id=TEST_USER_ID,
    session_id=session.id,
    message=TEST_MESSAGE,
):
    print(event['content']['parts'])