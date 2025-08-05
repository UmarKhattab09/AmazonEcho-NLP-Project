from fastapi import FastAPI,Request
from pydantic import BaseModel
from gradio_client import Client

app = FastAPI()
client = Client("UmarKhattab09/AmazonNLPproject",verbose=False)


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


