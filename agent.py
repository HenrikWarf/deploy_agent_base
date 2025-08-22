import os
import vertexai
import logging
from dotenv import load_dotenv
from google.adk.agents import Agent
from dotenv import load_dotenv
from vertexai import agent_engines


# Get environment variables
# -----------------------------------------
load_dotenv()
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
STAGING_BUCKET = os.getenv("STAGING_BUCKET")
AGENT_NAME = os.getenv("AGENT_NAME")
AGENT_MODEL = os.getenv("AGENT_MODEL")
AGENT_DESCRIPTION = os.getenv("AGENT_DESCRIPTION")
AGENT_INSTRUCTION = os.getenv("AGENT_INSTRUCTION")
APP_NAME = os.getenv("APP_NAME")
APP_DESCRIPTION = os.getenv("APP_DESCRIPTION")


# Validate that all required environment variables are set
if not all([PROJECT_ID, LOCATION, STAGING_BUCKET, AGENT_NAME, AGENT_MODEL, AGENT_DESCRIPTION, AGENT_INSTRUCTION, APP_NAME, APP_DESCRIPTION]):
    raise ValueError("Missing required environment variables. Please check your .env file.")



# Define a simple tool for the agent
# -----------------------------------------
def get_weather(city: str) -> str:
    """Gets the weather for a given city."""
    if "san francisco" in city.lower():
       return "It's foggy and 65 degrees in San Francisco."
    elif "new york" in city.lower():
        return "It's sunny and 75 degrees in New York."
    else:
        return f"I don't have the weather for {city}."


# Define and instantiate your ADK agent
# -----------------------------------------
print("Defining ADK agent...")
root_agent = Agent(
    name=AGENT_NAME,
    model=AGENT_MODEL,
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    tools=[get_weather],
 )


# Initialize Vertex AI
# ----------------------------------
logging.info("Initializing Vertex AI...")
try:
    # Initialize the Vertex AI SDK
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION,
        staging_bucket=STAGING_BUCKET
    )
except Exception as e:
    logging.error(f"Failed to initialize Vertex AI: {e}")
    exit(1)


# Deploy the agent to Vertex AI Agent Engine
# ----------------------------------
logging.info("Deploying agent to Vertex AI Agent Engine...")

try:
    remote_agent = agent_engines.create(
        agent_engine=root_agent,
        display_name=APP_NAME,
        description=APP_DESCRIPTION,
        requirements=["google-cloud-aiplatform[adk,agent_engines]",
                      "google-adk", 
                      "python-dotenv",
                      "pydantic",
                      "cloudpickle"]
    )
    logging.info(f"Agent deployed successfully!")
    logging.info(f"Resource Name: {remote_agent.resource_name}")
except Exception as e:
    logging.error(f"An error occurred during deployment: {e}")