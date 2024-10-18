from swarm import Swarm, Agent
from dotenv import load_dotenv  # Para cargar variables de entorno
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")

client = Swarm()

def get_weather(location)->str:
    """Get the weather for a given location"""
    return "{'temp': 67, 'unit': 'F'}"

agent = Agent(
    name="Agent Weather",
    instructions="You are a helpful agent",
    functions=[get_weather],
)

messages = [{"role":"user", "content":"What is the weather in New York?"}]

response = client.run(
    messages=messages,
    agent=agent,
)

print(response.messages[-1]["content"])