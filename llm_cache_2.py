import os 
from langchain_openai import OpenAI, ChatOpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain.globals import set_llm_cache

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    max_completion_tokens=100,
    temperature=0,
)

set_llm_cache(SQLiteCache(database_path=".langchain.db"))

prompt = [ 
    {'role': 'user',
    'content': 'Qual o melhor tipo de café? Me responda com uma frase'},
]

response = model.invoke(prompt)
print(f'Chamada 1:{response.content}')

response2 = model.invoke(prompt)
print(f'Chamada 1:{response2.content}')