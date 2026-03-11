from langchain_openai import ChatOpenAI
from orchestrator.coordinator import run_agents

query = input("Enter your research question: ")

result = run_agents(query)

print("\nFinal Answer:\n")
print(result)
