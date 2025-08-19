from vertexai.preview import adk

# Define a simple tool for the agent
@adk.tool
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
agent = adk.Agent(
    tools=[get_weather],
    model="gemini-1.5-flash-001"
)
