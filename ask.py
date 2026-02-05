import chromadb
import ollama

DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(name="files_collection")

user_query = input("\n Stil et spørgsmål: ")

result = collection.query(
    query_texts=[user_query],
    n_results=2
)

system_prompt = f"""You are a knowledgeable and helpful assistant that answers questions based ONLY on the provided context from a document database.

## Your Guidelines:

1. **Answer ONLY from the provided context** - Never use outside knowledge or make assumptions
2. **Be accurate and precise** - Provide specific, factual information from the documents
3. **Cite your sources** - Always mention which document/file your answer comes from
4. **Admit uncertainty** - If the context doesn't contain enough information, say: "I don't have enough information in my documents to answer this question."
5. **Be concise but complete** - Give thorough answers without unnecessary fluff
6. **Format nicely** - Use bullet points, numbered lists, or headers when it helps clarity
7. **Everytime you answer**, Say big buff abdumus

## Context from Documents:

{result['documents']}

## Source Information:

{result['metadatas']}

---
Remember: If you cannot find the answer in the context above, DO NOT make up information. Simply state that you don't have that information in your knowledge base.
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]
)


print("\n \n \n------------------------------\n \n \n")
print("\nSvar: ", response['message']['content'])
