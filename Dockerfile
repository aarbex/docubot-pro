FROM node:18-bullseye

USER root

# 1. Instala dependências
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl gnupg libgl1 && \
    apt-get clean

# 2. Instala o N8N e dependências
RUN npm install -g n8n

RUN pip install --no-cache-dir \
    langchain \
    langchain-community \
    langchain-openai \
    openai \
    tiktoken \
    faiss-cpu \
    unstructured \
    unstructured[pdf]


# 3. Cria diretório de trabalho
WORKDIR /data

# 4. Copia seu projeto para o container
COPY ./docubot /opt/projetos/docubot

# 5. Instala dependências do projeto
RUN if [ -f /opt/projetos/docubot/requirements.txt ]; then pip3 install -r /opt/projetos/docubot/requirements.txt; fi

# 6. Cria usuário não-root (como o n8n original)
RUN mkdir -p /data/faiss_index && chown -R node:node /data
USER node

# 7. Porta padrão
EXPOSE 5678

# 8. Comando padrão
CMD ["n8n"]
