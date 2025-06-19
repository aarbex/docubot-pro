# 🤖 DocuBot Pro

Plataforma inteligente de perguntas e respostas baseada em documentos, utilizando **RAG (Retrieval-Augmented Generation)** com **OpenAI**, **LangChain**, **FAISS**, **Python** e automações com **N8N**.

---

## 📚 Descrição

O **DocuBot Pro** é uma solução que permite consultar automaticamente o conteúdo de documentos internos (PDFs, .txt, .docx), oferecendo respostas contextuais com inteligência artificial, por meio do modelo GPT-4 da OpenAI, utilizando o conceito de RAG.

Ideal para áreas como:
- Jurídico
- RH
- Compliance
- Suporte interno
- Consultorias

---

## ⚙️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [LangChain](https://www.langchain.com/)
- [OpenAI](https://platform.openai.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [N8N](https://n8n.io/)
- [Docker](https://www.docker.com/)
- HTML + CSS + FontAwesome

---

## 🚀 Funcionalidades

✅ Upload de documentos  
✅ Indexação automática com FAISS  
✅ Consulta por pergunta natural  
✅ IA treinada nos próprios arquivos  
✅ Front-end leve e responsivo  
✅ Fluxo automatizado via N8N (opcional)

---

## 🖥️ Demonstração

![docubot-preview](https://via.placeholder.com/800x400?text=Prévia+da+interface+DocuBot+Pro)

---

## 🛠️ Como usar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/docubot.git
cd docubot

---

## 🛠️ Como usar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/docubot.git
cd docubot
````

### 2. Crie o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da OpenAI

Crie o arquivo `.env` com:

```env
OPENAI_API_KEY=sk-xxxxxxx
```

### 5. Coloque arquivos em `docs/` e indexe

```bash
python index_docs.py
```

### 6. Inicie a interface

```bash
flask run
```

Acesse [http://localhost:5000](http://localhost:5000)

---

## 🔄 Integração com N8N (opcional)

Um fluxo N8N está disponível para:

* Receber perguntas via Webhook
* Executar o script Python `query_engine.py`
* Retornar respostas via e-mail, Slack, Telegram, etc.

Importe o arquivo `docubot-workflow.json` no painel do N8N.

---

## 📂 Estrutura

```
docubot/
├── app.py               # Front-end Flask
├── index_docs.py        # Indexação FAISS
├── query_engine.py      # Consulta com RAG
├── docs/                # Documentos do usuário
├── faiss_index/         # Índices vetoriais
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .env
├── .gitignore
└── requirements.txt
```

---

## 📄 Licença

MIT © [Seu Nome ou Organização](https://github.com/aarbex)

---

## 🤝 Contribuições

Pull requests são bem-vindos. Para sugestões, abra uma issue.

---

## 📬 Contato

Entre em contato pelo [LinkedIn](https://www.linkedin.com/in/andr%C3%A9-elias-alves-arbex-26278b23/) ou envie um e-mail para [arbex.andre@gmail.com](mailto:arbex.andre@gmail.com).

````

