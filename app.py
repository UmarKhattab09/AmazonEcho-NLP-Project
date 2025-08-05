from fastapi import FastAPI,Request
from pydantic import BaseModel
from gradio_client import Client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
client = Client("UmarKhattab09/AmazonNLPproject",verbose=False)
origins = [
    "http://localhost:3000",
    "https://amazon-echo-nlp-project.vercel.app",
    "*"  # Only use "*" in development!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows your frontend domain
    allow_credentials=True,
    allow_methods=["*"],    # Allow all HTTP methods: GET, POST, etc.
    allow_headers=["*"],    # Allow all headers
)

@app.get("/")
def root():
    return {"message":"Welcome to AI "}

# class UrlInput(BaseModel):
#     url: str

@app.post("/review")
async def getdataframe(request: Request):
    data = await request.json()
    url = data["url"]
    # question = data["question"]
    df = client.predict(url, api_name="/dfreviews")
    return {"columns": df.columns.tolist(), "rows": df.head(10).to_dict(orient="records")}

# class Answer(BaseModel):
#     url:str
#     question:str

@app.post("/ans")
async def ask_question(request: Request):
    data = await request.json()
    url = data["url"]
    question = data["question"]
    answer = client.predict(url,question,api_name="/getans")
    # answer = getans(url, question)
    return {"answer": answer}


