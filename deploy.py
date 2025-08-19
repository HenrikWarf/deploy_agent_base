
import os
import vertexai
from dotenv import load_dotenv
from vertexai.preview import agent_engines
from agent import agent

# Load environment variables from .env file
load_dotenv()

# Get environment variables
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
STAGING_BUCKET = os.getenv("STAGING_BUCKET")

# Validate that all required environment variables are set
if not all([PROJECT_ID, LOCATION, STAGING_BUCKET]):
    raise ValueError("Missing required environment variables. Please check your .env file.")

print("Initializing Vertex AI...")
# Initialize the Vertex AI SDK
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET
)

# Deploy the agent to Vertex AI Agent Engine
print("Deploying agent to Vertex AI Agent Engine...")
try:
    remote_agent = agent_engines.create(
        local_agent=agent,
        display_name="My Weather Agent",
        description="An agent that provides weather information.",
        requirements=[], # No third-party packages needed for this simple agent
    )
    print(f"Agent deployed successfully!")
    print(f"Resource Name: {remote_agent.resource_name}")
except Exception as e:
    print(f"An error occurred during deployment: {e}")

