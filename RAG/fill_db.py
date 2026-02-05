from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb


DATA_PATH = r'data'
CHROMA_PATH = r'chroma_db'

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(name="files_collection")

# Load markdown files
md_loader = DirectoryLoader(DATA_PATH, glob="**/*.md", loader_cls=TextLoader)
md_documents = md_loader.load()
print(f"Loaded {len(md_documents)} markdown documents")

# Load PDF files
pdf_loader = DirectoryLoader(DATA_PATH, glob="**/*.pdf", loader_cls=PyPDFLoader)
pdf_documents = pdf_loader.load()
print(f"Loaded {len(pdf_documents)} PDF documents")

# Combine all documents
raw_documents = md_documents + pdf_documents
print(f"Total: {len(raw_documents)} documents")

# den her kan blive meget mere crazy det er bare basic lige nu splittet kan blive vildere og det burde det også blive på et tidsapunkt :D
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200, 
    length_function=len,
    is_separator_regex=False,
)
documents = text_splitter.split_documents(raw_documents)
# preparing to be added in chromadb

document = []
metadata = []
# grunden til vi gør det her er for at vi kan se chinksne i vores VEKTOR DB senere
ids = []

i = 0

for chunk in documents:
    document.append(chunk.page_content)
    metadata.append(chunk.metadata)
    ids.append(f"doc_{i}")
    i += 1


    collection.upsert(
        documents=document,
        metadatas=metadata,
        ids=ids
    )