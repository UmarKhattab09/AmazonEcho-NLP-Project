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



def dfreviews(url):
    emb = Embedded(url)
    df = emb.websitename()
    pineconedf = emb.namespace()
    return df
    
def getans(question):
    pass


## REMINDER TO MYSELF TO CHANGE THE models to online models when pushing to huggingfacespace


def main():
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                gr.HTML('<h1> Amazon Web Scraping.')
            with gr.Column():
                gr.HTML("<p> The concept is taken from RUFUS AI of Amazon. It's basically taking link and give a brief description of the product")

        with gr.Row():
            with gr.Column():
                dataframe = gr.Dataframe(headers=["Reviews"],datatype=["str"])
            with gr.Column():  
                url = gr.Textbox(label="Give Link")  
                range = gr.Button("Load DataFrame")
                range.click(dfreviews,inputs=[url],outputs=[dataframe])

        with gr.Row():
            with gr.Column():
                question = gr.Textbox(label="Provide a question about the product")
                anstextbox = gr.Textbox(label="answer")
                ans = gr.Button("Load Answer")
                ans.click(getans,inputs=[question],outputs=[anstextbox])
                
                



    demo.launch()



if __name__ =="__main__":
    main()
