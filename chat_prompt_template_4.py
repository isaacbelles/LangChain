import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOpenAI(
    model='gpt-4o-mini',
    max_completion_tokens=100,
    temperature=0,
)

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content='Você deve responder baseado em dados geográficos do Brasil.'),
        HumanMessagePromptTemplate.from_template('Por favor, me fale sobre a região {regiao}.'),
        AIMessage(content='Claro, vou começar coletando informaço2es sobre a região e analisando os dados disponíveis.'),
        HumanMessage(content='Certifique-se de incluir dados demográficos.'),
        AIMessage(content='Entendido. Aqui estão os dados:'),
    ]
)

prompt = chat_template.format_messages(regiao='Sul')

response = model.invoke(prompt)

print(response.content)
