from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI

# Outras importações necessárias
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

import sys

if len(sys.argv) < 2:
    print("Argumentos recebidos:", sys.argv)
    sys.exit(1)

query = sys.argv[1]
#query = "qual a política de home office da empresa?"

db = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)

# Define o retriever
retriever = db.as_retriever()


qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4"),
    retriever=retriever
)


docs = db.similarity_search(query)
llm = ChatOpenAI()
chain = load_qa_chain(llm, chain_type="stuff")
response = chain.run(input_documents=docs, question=query)

print(response)

'''
def query_rag(question: str) -> str:
    db = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-4"),
        retriever=retriever
    )
    return qa.run(question)
    '''