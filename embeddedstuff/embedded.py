import os
import sys


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from WebsiteScrap import WebsiteScrapper
import pandas as pd 
from dotenv import load_dotenv
load_dotenv()
from pinecone import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings
from pinecone.grpc import PineconeGRPC as Pinecone


class Embedded:
    def __init__(self,url):
        self.url = url

    def websitename(self):
        web = WebsiteScrapper(self.url)
        dfname = web.websitename()
        print(dfname)
        try:
            df = pd.read_csv(f"outputs/{dfname}.csv")
            return df
        except:
            print(f"NO FILE EXIS. Creating One")
            df = web.scraping()
            return df
        
    def load_embmodel(self):
        # model_name = "E:\\models\\gte-small"
        model_name = "thenlper/gte-small"
        embedding_model = HuggingFaceEmbeddings(
            model_name=model_name,
            multi_process=False,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},  # Set `True` for cosine similarity
        )
        return embedding_model
    def vectorized(self):
        PINECONE = os.getenv("PINECONE")
        pc = Pinecone(api_key=PINECONE)
        index = pc.Index("amazon")
        web = WebsiteScrapper(self.url)
        dfname = web.websitename()
        embedded_model = self.load_embmodel()
        print("Initializing Index-------------") 
        print("Now Converting Data into Vectorized Input")
        data = []
        # print(df)
        df = self.websitename()
        for i in range(len(df)): ### REMINDING MYSELF IF SOME ERROR OCCURS AGAINST DF. I'VE NOT IMPORTED HERE ### UPDATE: IT DID
            print(f"Starting for data vectorized of {i} data")
            text = df[dfname][i]
            vector = embedded_model.embed_query(text)
            data.append(
                {
                    "id":"vec{}".format(i),
                    "values":vector,
                    "metadata":{"text":text}
                }
            )
        print("Completed Data Vectorized")
        
        
        return data
    



    def namespace(self):
        web = WebsiteScrapper(self.url)
        PINECONE = os.getenv("PINECONE")
        pc = Pinecone(api_key=PINECONE)
        dfname = web.websitename()
        index = pc.Index(host="https://amazon-f8neck5.svc.aped-4627-b74a.pinecone.io")
        indexlist =index.describe_index_stats()

        if dfname in indexlist['namespaces']:
            print("Data already exist in Database")

        else:
            print("Doesn't Exist, Creatnng one now")
            df = self.websitename()
            print("Created DF")
            print("NOW CREATING VECTORIZING DATA")
            vectorized = self.vectorized()
            print("Created Vectowerized DATA")
            print("PUSHING DATA")
            index.upsert(
                vectors=vectorized,
                namespace=dfname
            )
            return vectorized
        
        
            



            
    



# url = "https://www.amazon.com/Charger-charging-Certified-lightning-AirPods/dp/B0B283QP2N/?_encoding=UTF8&pd_rd_w=xI3Mi&content-id=amzn1.sym.117cb3e1-fd12-46a0-bb16-15cd49babfdb%3Aamzn1.symc.abfa8731-fff2-4177-9d31-bf48857c2263&pf_rd_p=117cb3e1-fd12-46a0-bb16-15cd49babfdb&pf_rd_r=1A0Y3SCKF61QZME5WKSB&pd_rd_wg=ZWwxr&pd_rd_r=ae81b6c3-d9bd-471e-908b-d82eca3bdbf3&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d"
# test = Embedded(url)

# test2 = test.namespace()
    
