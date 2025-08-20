import getpass
import os
from langchain_openai import OpenAI, ChatOpenAI

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    temperature=1,
    max_completion_tokens=250
)

messages = [
    {'role': 'system', 'content': 'Você é um assistente virtual especializado em café.'},
    {'role': 'user', 'content': 'Me responda qual o melhor tipo de grão de café. Me responda com no máximo 250 caractéres.'},
]

response = model.invoke(messages)

print(response)
print(response.content)