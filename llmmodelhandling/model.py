
import os 
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from WebsiteScrap import WebsiteScrapper
from embeddedstuff import Embedded
from transformers import AutoModelForCausalLM 
from transformers import AutoTokenizer
from transformers import pipeline
import torch
from pinecone import Pinecone
from dotenv import load_dotenv
load_dotenv()

class llmmodel:
    def __init__(self,user_input,url):
        self.model_name="E:\\models\\pleasRAG"
        self.user_input = user_input
        self.url = url

    def llmmodel(self):
        model = AutoModelForCausalLM.from_pretrained(self.model_name)
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            return_full_text=True
        )

        return pipe
        

    def context(self):
        web = WebsiteScrapper(self.url)
        emb = Embedded(self.url)
        embedding_model=emb.load_embmodel()
        dfname = web.websitename()
        PINECONE = os.getenv("PINECONE")
        pc = Pinecone(api_key=PINECONE)
        index = pc.Index("amazon")
        try:
            vectorized_input = embedding_model.embed_query(self.user_input)
            context = index.query(
                namespace=dfname,
                vector=vectorized_input,
                top_k=2,
                include_metadata=True
            )
            combinedcontext = [context['matches'][i]['metadata']['text'] for i in range(len(context['matches']))]
            combinedcontext=str(".".join(combinedcontext))
            return combinedcontext
        except:
            return f"ERROR NO DATABASE"

    def feedback(self):
        contextfromdb = self.context()
        pipe = self.llmmodel()
        prompt = "Answer the questions about the product based on the userinput{userinput} and having sources {sources}"
        answer = pipe(prompt.format(userinput=self.user_input,sources = contextfromdb))

        return answer[0]['generated_text']

        

# url = "https://www.amazon.com/Amazon-Basics-Everyday-Plates-Disposable/dp/B0C2CY22B8/?_encoding=UTF8&pd_rd_w=APjaP&content-id=amzn1.sym.f2128ffe-3407-4a64-95b5-696504f68ca1&pf_rd_p=f2128ffe-3407-4a64-95b5-696504f68ca1&pf_rd_r=YXMEXN435CNCQZWD512A&pd_rd_wg=7Izqy&pd_rd_r=3fbb0d02-8f22-4b11-ac45-f11f9ef282d6&ref_=pd_hp_d_btf_crs_zg_bs_284507&th=1"
# userinput = "What do you think about the product"
# test = llmmodel(url=url,user_input=userinput)

# feed= test.context()
# print(feed)
# ans = test.feedback()
