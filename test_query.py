from vertexai import agent_engines
import uuid
import asyncio
import sys


async def main():
  
    agent = agent_engines.get("projects/ml-developer-project-fe07/locations/us-central1/reasoningEngines/5145635253154480128")
    print(agent)

    user_id = str(uuid.uuid4())
    #session_id = str(uuid.uuid4())
    #print(f"Querying agent with session_id: {session_id}")
    #session = await agent.async_create_session(user_id=session_id)

    async for event in agent.async_stream_query(
        user_id=user_id,
    #    session_id=session,  # Optional
        message="What is the weather in New york?",
    ):
        try:
            print(event['content']['parts'][0]['text'])
        except:
            pass

if __name__ == "__main__":
    # Run the asynchronous main function
    asyncio.run(main())






