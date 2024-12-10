from fastapi import FastAPI
from utils.llm_chat_interface import create_response
# Initialize the FastAPI app
app = FastAPI()

# Define a route (endpoint)
@app.get("/hello")
async def read_hello():
    return {"message": "Hello, World!"}

@app.get("/inference/{content}")
async def inference(content: str):

    response = create_response(content)
    if response:
        return {"message": response.choices[0].message.content}
    return {"message": "query failed"}


