import os
import uuid
import asyncio
from dotenv import load_dotenv
from vertexai import agent_engines

# Load environment variables from .env file
load_dotenv()

# Get environment variables
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
REASONING_ENGINE_ID = os.getenv("REASONING_ENGINE_ID")

# Validate that all required environment variables are set
if not all([PROJECT_ID, LOCATION, REASONING_ENGINE_ID]):
    raise ValueError("Missing required environment variables. Please set PROJECT_ID, LOCATION, and REASONING_ENGINE_ID in your .env file.")

async def main():
  
    agent = agent_engines.get(f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{REASONING_ENGINE_ID}")
    print(agent)

    user_id = str(uuid.uuid4())

    async for event in agent.async_stream_query(
        user_id=user_id,
        message="What is the weather in New york?",
    ):
        try:
            print(event['content']['parts'][0]['text'])
        except:
            pass

if __name__ == "__main__":
    # Run the asynchronous main function
    asyncio.run(main())






