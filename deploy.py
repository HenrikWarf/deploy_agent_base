
import os
import vertexai
import logging
from dotenv import load_dotenv
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp


#---------------------------------------------
# Environment Variables
# Load environment variables from .env file
load_dotenv()

# Get environment variables
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
STAGING_BUCKET = os.getenv("STAGING_BUCKET")

# Validate that all required environment variables are set
if not all([PROJECT_ID, LOCATION, STAGING_BUCKET]):
    raise ValueError("Missing required environment variables. Please check your .env file.")

#-------------------------------------------
# Logging

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

#-------------------------------------------
# Deployment

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

app = AdkApp(
   agent='agent_instructions.root_agent',
   enable_tracing=True
)
logging.debug("deploying agent to agent engine:")

# Deploy the agent to Vertex AI Agent Engine
logging.info("Deploying agent to Vertex AI Agent Engine...")

#-------------------------------------------
# Agent Configuration
# TODO: Customize the display name and description of your agent
AGENT_DISPLAY_NAME = "My Weather Agent"
AGENT_DESCRIPTION = "An agent that provides weather information."
#-------------------------------------------

try:
    remote_agent = agent_engines.create(
        agent_engine=app,
        display_name=AGENT_DISPLAY_NAME,
        description=AGENT_DESCRIPTION,
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

