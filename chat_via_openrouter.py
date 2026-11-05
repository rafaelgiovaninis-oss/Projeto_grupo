import os

from langchain_openrouter import ChatOpenRouter

from dotenv import load_dotenv

load_dotenv()


print("API KEY:", os.getenv("OPENROUTER_API_KEY"))

llm = ChatOpenRouter(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
)

controlador = True

while controlador == True:

    pergunta = str(input("Qual sua pergunta?: "))

    if pergunta == "":
        break

    response = llm.invoke(pergunta)

    print(response.content)

#python chat_via_openrouter.py