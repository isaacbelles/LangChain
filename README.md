# LangChain Exemplos

Este repositório contém exemplos práticos de uso da biblioteca **LangChain** com modelos da **OpenAI**, mostrando diferentes formas de criar:

- Assistentes virtuais  
- Chains  
- Roteamento de perguntas  
- Tradução  
- Cache de respostas  
- Templates de prompt  

---

## Sumário dos Arquivos

1. **hello_world_1.py**  
   Exemplo básico de um assistente virtual especializado em café.  
   O usuário pergunta sobre grãos de café e recebe uma resposta curta do modelo.  

2. **llm_cache_2.py**  
   Demonstra como utilizar **cache (SQLite)** para armazenar e reutilizar respostas do modelo, evitando chamadas repetidas à API.  

3. **template_3.py**  
   Exemplo de tradução de texto entre idiomas usando um template de prompt customizado.  

4. **chat_prompt_template_4.py**  
   Cria uma cadeia de mensagens simulando uma conversa sobre dados geográficos do Brasil, incluindo instruções para o modelo responder com dados demográficos.  

5. **simple_chain_5.py**  
   Gera respostas sobre linguagens de programação usando um prompt simples e direto.  

6. **router_chain_6.py**  
   Implementa um **roteador de perguntas**: classifica a dúvida do usuário e direciona para o setor correto (Financeiro, Suporte Técnico ou Informações Gerais), retornando uma resposta personalizada.  

---

##  Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/langchain-examples.git
cd langchain-examples
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv .venv

# Linux / Mac
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure sua chave da OpenAI
Defina a variável de ambiente **OPENAI_API_KEY**:

```bash
# Linux / Mac
export OPENAI_API_KEY="sua_chave_aqui"

# Windows (PowerShell)
setx OPENAI_API_KEY "sua_chave_aqui"
```

### 5. Execute um exemplo
Escolha o arquivo desejado e rode com Python. Exemplo:
```bash
python hello_world_1.py
```
