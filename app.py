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

def dfreviews(url):
    emb = Embedded(url)
    df = emb.websitename()
    pineconedf = emb.namespace()
    return df
    
def getans(url,question):
    ans = llmmodel(user_input=question,url=url)
    answer = ans.feedback()
    return answer


## REMINDER TO MYSELF TO CHANGE THE models to online models when pushing to huggingfacespace


def main():
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                gr.HTML('<h1> Amazon Web Scraping.')
            with gr.Column():
                gr.HTML("<p> The concept is taken from RUFUS AI of Amazon. It's basically taking link and give a brief description of the product. Most links may not work because I can not scrap them without permission and the dataset isn't large.")
        with gr.Row():
            with gr.Column():
                dataframe = gr.Dataframe(headers=["Reviews"],datatype=["str"])
            with gr.Column():  
                url = gr.Textbox(label="Give Link")  
                range = gr.Button("Load DataFrame")
                range.click(dfreviews,inputs=[url],outputs=[dataframe])

        with gr.Row():
            with gr.Column():
                gr.HTML("<p> So the problem is prompt engineering or the model im using is not the best. It's trained on 1b paramter I just downloaded it for saving time. I will fix it soon.</p>")
                url = gr.Textbox(label="Give Link")  
                question = gr.Textbox(label="Provide a question about the product")
                anstextbox = gr.Textbox(label="answer")
                ans = gr.Button("Load Answer")
                ans.click(getans,inputs=[url,question],outputs=[anstextbox])
                
                



    demo.launch()



if __name__ =="__main__":
    main()
