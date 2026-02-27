
from config.db import get_chroma_client, get_collection
from models.message import Messages, Query
from ollama import AsyncClient

class RAGService:
    def __init__(self):
        self.chroma_client = get_chroma_client()
        self.collection = get_collection(self.chroma_client)
        self.client = AsyncClient()

    def system_prompt(self, documents: list, metadatas: list) -> str:
                   
            return  f"""You are a knowledgeable and helpful assistant that answers questions based ONLY on the provided context from a document database.

            ## Your Guidelines:

            1. **Answer ONLY from the provided context** - Never use outside knowledge or make assumptions
            2. **Be accurate and precise** - Provide specific, factual information from the documents
            3. **Cite your sources** - Always mention which document/file your answer comes from
            4. **Admit uncertainty** - If the context doesn't contain enough information, say: "I don't have enough information in my documents to answer this question."
            5. **Be concise but complete** - Give thorough answers without unnecessary fluff
            6. **Format nicely** - Use bullet points, numbered lists, or headers when it helps clarity
            7. **Everytime you answer**, Say: HELLO BIG BOSS ABDU

            ## Context from Documents:

            {documents}

            ## Source Information:

            {metadatas}

            ---
            Remember: If you cannot find the answer in the context above, DO NOT make up information. Simply state that you don't have that information in your knowledge base"""


    async def query(self, request: Query) -> Messages:
       
        search_result = self.collection.query(
            query_texts=[request.query],
            n_results=request.top_k )
        flat_documents = search_result['documents'][0] if search_result['documents'] else []
        flat_results = [dict(m) for m in search_result['metadatas'][0]] if search_result['metadatas'] else []    

        prompt = self.system_prompt(flat_documents, flat_results)

        response = await self.client.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": request.query}
            ]
        )

        answer = response['message']['content']

        return Messages(
            source_documents=flat_documents,    
            content=request.query,
            answer=answer,
            results=flat_results,
            query_id=request.query_id,
            role="assistant",
        )