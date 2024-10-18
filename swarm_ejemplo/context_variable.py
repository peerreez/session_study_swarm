from swarm import Swarm, Agent
from dotenv import load_dotenv  # Para cargar variables de entorno
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")

client = Swarm()

def instructions(context_variables):
    name = context_variables.get("name","User")
    return f"You are a helpful agent. Greet the user by name({name})."

def print_account_details(context_variables: dict):
    user_id = context_variables.get("user_id",None)
    name = context_variables.get("name",None)
    print(f"Account details for user {name} (ID: {user_id})")
    return "Success"

agent = Agent(
    name="Agent",
    instructions=instructions,
    functions=[print_account_details],
)

context_variables = {
    "name": "John Doe",
    "user_id": "1234567890"
}

response = client.run(
    messages=[{"role": "user", "content":"Hi"}], 
    agent=agent, 
    context_variables=context_variables,
    )
print(response.messages[-1]["content"])

response = client.run(
    messages=[{"role": "user", "content":"Print my account details!"}], 
    agent=agent, 
    context_variables=context_variables,
    )
print(response.messages[-1]["content"])