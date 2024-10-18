from swarm import Swarm, Agent
from dotenv import load_dotenv  # Para cargar variables de entorno
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")
client = Swarm()

agent = Agent(
    name="Bare Minimum Agent",
    instructions="You are a helpful assistant.",
)

messages = [{"role": "user", "content": "HI!"}]
response = client.run(agent=agent, messages=messages)
print(response.messages[-1]["content"])
