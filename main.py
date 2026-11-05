import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Carrega variáveis de ambiente
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
print("API key loaded:", bool(api_key))

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=api_key,
)

pergunta = str(input("Qual sua pergunta?"))

response = llm.invoke(pergunta)

print(response)