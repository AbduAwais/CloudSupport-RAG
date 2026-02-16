from fastapi import FastAPI
from api.routes.main import router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/")
async def root():
    return {"message": "RAG API is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)