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




