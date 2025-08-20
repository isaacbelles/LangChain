import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

model = ChatOpenAI(
    model='gpt-4o-mini',
    max_completion_tokens=100,
    temperature=0,
)

template = '''
Traduza o texto do {idioma1} para o {idioma2}:
{texto}
'''
prompt_template = PromptTemplate.from_template(
    template= template
)

prompt = prompt_template.format(
    idioma1='português',
    idioma2='alemão',
    texto='Bom dia!',
)

response = model.invoke(prompt)
print(response.content)
 