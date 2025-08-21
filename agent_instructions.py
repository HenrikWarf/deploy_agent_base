import os
from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()

# Define a simple tool for the agent
def get_weather(city: str) -> str:
    """Gets the weather for a given city."""
    if "san francisco" in city.lower():
       return "It's foggy and 65 degrees in San Francisco."
    elif "new york" in city.lower():
        return "It's sunny and 75 degrees in New York."
    else:
        return f"I don't have the weather for {city}."

# Define and instantiate your ADK agent
print("Defining ADK agent...")
root_agent = Agent(
    name="weather_test_agent",
    model="gemini-2.5-flash",
    description="Agent to answer questions about the weather in a city.",
    instruction=(
        "You are a helpful agent who can answer user questions about the weather in a city."
    ),
    tools=[get_weather],

 )
