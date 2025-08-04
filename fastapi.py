import os
import sys
import gradio as gr
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from WebsiteScrap import WebsiteScrapper
from embeddedstuff import Embedded
import pandas as pd 
from dotenv import load_dotenv
load_dotenv()
from pinecone import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from llmmodelhandling import llmmodel
# import lightning as L
# from lightning.app.components import PythonServer

from backend import getans, dfreviews
from pydantic import BaseModel


from fastapi import FastAPI,Request
app=FastAPI()



@app.get("/")
def root():
    return {"message":"Welcome to AI "}
@app.post("/extract-data")

async def extract_data(request: Request):
    data = await request.json()
    url = data["url"]
    df = dfreviews(url)
    return {"columns": df.columns.tolist(), "rows": df.head(10).to_dict(orient="records")}

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    url = data["url"]
    question = data["question"]
    answer = getans(url, question)
    return {"answer": answer}