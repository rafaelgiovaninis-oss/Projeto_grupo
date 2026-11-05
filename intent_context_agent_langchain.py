import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

llm = ChatOpenRouter(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
)

# Biblioteca de conceitos
CONTEXTS = {
    "mcp": """
MCP (Model Context Protocol):
- protocolo para padronizar como contexto, ferramentas e memória são fornecidos ao LLM
- desacoplamento entre modelo e sistemas externos
""",

    "rag": """
RAG (Retrieval-Augmented Generation):
- recuperação de dados externos (docs, DB, embeddings)
- resposta baseada em contexto recuperado
""",

    "agentes": """
Agentes:
- entidades que tomam decisões e executam ações
- podem usar ferramentas, memória e planejamento
""",

    "langchain": """
LangChain:
- framework de orquestração de LLMs
- criação de chains, agents e integração com ferramentas
"""
}

def normalize(text: str) -> str:
    return text.lower()

def detect_concepts(user_input: str):
    text = normalize(user_input)
    found = []

    if "mcp" in text:
        found.append("mcp")
    if "rag" in text:
        found.append("rag")
    if "agente" in text or "agent" in text:
        found.append("agentes")
    if "langchain" in text:
        found.append("langchain")

    return found if found else ["default"]


def build_prompt(user_input: str) -> str:
    concepts = detect_concepts(user_input)

    context_block = "\n".join(
        CONTEXTS[c] for c in concepts if c in CONTEXTS
    )

    return f"""
Você é um especialista em IA moderna.

Considere os seguintes conceitos:
{context_block}

Explique de forma integrada, conectando os conceitos quando fizer sentido.

Pergunta:
{user_input}
"""


#Teste
user_input = "Fale sobre LangChain e MCP em uma frase"

prompt = build_prompt(user_input)
print(prompt)
response = llm.invoke(prompt)
print(response.content)