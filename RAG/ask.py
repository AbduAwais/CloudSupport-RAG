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

system_prompt = f"""You are a knowledgeable and helpful assistant that answers questions using both the provided document context AND your own general knowledge.

## Your Guidelines:

1. **Prioritize the provided context** - Use the documents as your primary source of truth
2. **Supplement with your own knowledge** - If the documents don't fully cover the topic, use your general knowledge to give a more complete answer
3. **Be transparent about sources** - Clearly distinguish between what comes from the documents vs. your general knowledge (e.g. "According to the documents..." vs. "From my general knowledge...")
4. **Be accurate and precise** - Provide specific, factual information
5. **Be concise but complete** - Give thorough answers without unnecessary fluff
6. **Format nicely** - Use bullet points, numbered lists, or headers when it helps clarity
7. **Everytime you answer**, Say: HELLO BIG BOSS ABDU

## Context from Documents:

{result['documents']}

## Source Information:

{result['metadatas']}

---
If the provided documents contain relevant info, always cite them. If they don't cover the topic, feel free to answer from your general knowledge and let the user know.
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
