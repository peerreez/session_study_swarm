from swarm import Swarm, Agent
from dotenv import load_dotenv  # Para cargar variables de entorno
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")
client = Swarm()

english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",
)

spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You only speak Spanish.",
)

def transfer_to_spanish_agent():
    """Trans spanish sepeaking users immediately"""
    return spanish_agent

english_agent.functions.append(transfer_to_spanish_agent)

messages = [{"role": "user", "content": "Hola, como estas?"}]
response = client.run(
    agent=english_agent,
    messages=messages,
)

print(response.messages[-1]["content"])

