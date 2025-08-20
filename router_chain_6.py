import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    max_completion_tokens=250,
    temperature=1,
)

classification_chain = (
    PromptTemplate.from_template(

        '''
        Classifique a pergunta do usuário em um dos seguintes setores:
        - Financeiro
        - SUporte Técnico
        - Outras Informações

        Pergunta: {pergunta}

        '''

    )
    |model
    |StrOutputParser()
)

financial_chain=(
    PromptTemplate.from_template(

        '''
        Você é um especialista financeiro.
        Sempre responda as perguntas começando com "Bem-vindo ao Setor Financeiro".
        Responda à pergunta do usuário:

        Pergunta: {pergunta}

        '''
    )
    |model
    |StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(

        '''
        Você é um especialista em suporte técnico.
        Sempre responda as perguntas começando com "Bem-vindo ao Suporte Técnico".
        Responda à pergunta do usuário:

        Pergunta: {pergunta}

        '''
    )
    |model
    |StrOutputParser()
)

other_info_chain = (
    PromptTemplate.from_template(

        '''
        Você é um assistente de informações gerais.
        Sempre responda as perguntas começando com "Bem-vindo ao setor de Central de Informações".
        Responda à pergunta do usuário:

        Pergunta: {pergunta}

        '''
    )
    |model
    |StrOutputParser()
)

def route(classification):
    classification = classification.lower()
    if 'financeiro' in classification:
        return financial_chain
    elif 'técnico' in classification:
        return tech_support_chain
    else:
        return other_info_chain
    
pergunta = input('Qual a sua dúvida?')

classification =  classification_chain.invoke(
    {'pergunta': pergunta}
)   

response_chain = route(classification=classification)

response = response_chain.invoke( 
    {'pergunta': pergunta}
)
print(response)