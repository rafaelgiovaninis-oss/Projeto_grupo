import os

from langchain_openrouter import ChatOpenRouter

from dotenv import load_dotenv

from pyscript import document

load_dotenv()


print("API KEY:", os.getenv("OPENROUTER_API_KEY"))

llm = ChatOpenRouter(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
)

def Enviar_pergunnta(Event):

    campo = document.querySelector( '#campo-pergunta' )
    
    pergunta = campo.value

    response = llm.invoke(pergunta)

    div_resposta = document.querySelector("#mensagens")
    div_resposta.innerText = response

#python chat_via_openrouter.py