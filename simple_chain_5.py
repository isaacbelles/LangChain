import os 
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    max_completion_tokens=250,
    temperature=1,
)

runnable_sequence = (
    PromptTemplate.from_template(
        'Me fale sobre a linguagem de programação: {linguagem}.'
    )
    |model
    |StrOutputParser()
)
response = runnable_sequence.invoke({'linguagem': 'Python'})

print(response)