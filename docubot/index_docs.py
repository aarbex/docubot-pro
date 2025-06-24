import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain.document_loaders import DirectoryLoader

import pandas as pd
import pdfplumber

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

# === PDF Tables ===
def extract_tables_from_pdfs(path):
    table_docs = []
    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            with pdfplumber.open(os.path.join(path, filename)) as pdf:
                for i, page in enumerate(pdf.pages):
                    tables = page.extract_tables()
                    for table in tables:
                        if not table or not all(isinstance(row, list) for row in table):
                            continue  # ou log a inconsistência
                        if table:
                            table_str = "\n".join(["\t".join(str(cell) if cell is not None else "" for cell in row) for row in table])
                            content = f"Tabela extraída do PDF ({filename}, página {i+1}):\n{table_str}"
                            table_docs.append(Document(page_content=content, metadata={"source": filename}))
    return table_docs

# === CSV / XLSX ===
def load_tabular_files(path):
    tabular_docs = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if file.endswith(".csv"):
            df = pd.read_csv(full_path)
        elif file.endswith(".xlsx"):
            df = pd.read_excel(full_path)
        else:
            continue
        if not df.empty:
            table_str = df.to_markdown(index=False)
            content = f"Tabela convertida de arquivo {file}:\n{table_str}"
            tabular_docs.append(Document(page_content=content, metadata={"source": file}))
    return tabular_docs

# === Texto Geral ===
def load_text_documents(path):
    loader = DirectoryLoader(path, glob="**/*.pdf", recursive=True)
    return loader.load()

def index_documents():
    print("📄 Carregando documentos...")
    docs_texto = load_text_documents('./docs')
    docs_tabelas = load_tabular_files('./docs')
    docs_pdf_tables = extract_tables_from_pdfs('./docs')

    print(f"🔢 Documentos: {len(docs_texto)}, Tabelas: {len(docs_tabelas)}, Tabelas PDF: {len(docs_pdf_tables)}")

    all_docs = docs_texto + docs_tabelas + docs_pdf_tables
    chunks = splitter.split_documents(all_docs)

    print(f"🧠 Total de chunks para indexação: {len(chunks)}")
    db = FAISS.from_documents(chunks, OpenAIEmbeddings())
    db.save_local("faiss_index")
    print("✅ Indexação concluída.")

if __name__ == "__main__":
    index_documents()
