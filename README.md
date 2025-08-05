# AmazonEcho-NLP-Project

### MOREUPDATES 
- Gradioapp.py consist of Gradio UI
- oldapp.py consisnt of FastAPI but it can not be used as a backend because it requires a lot of cpu power
- im building a fast api wrapper that will use huggingface gradio client and just transport the data,hopefully it works


## What I have done 
- In NLP BASICS, you will find the basics of NLP, Tokkenizaion,stemming,BOW,TFIDF etc...
- Right now I am trying to create something similar to RUFUS AI that amazon uses, it won't be fast but just for learning stuff



## What have I tried so far
- I am currently trying to create a algorithm that takes the link and extract the reviews and save it in a dataframe
- as of now, I have tried illama model but it was not giving the output I was liking so I will try different models. I need to try a RAG illama model. I was trying a simple one.
- I also tried a random RAG model call Pelvias RAG 1B its not good but it shows that its working.
- Will create an app that supports Gradio and will add in my mcp project. 


## Stuff
- I am also using a pinecone api key that will take the dataset and use a huggingface model to embedded it and save it at a pinecone api. I will make something like when a new link is inserted and there is no database for it. It will create one.
- Let's see how far I can take it.



# AS OF NOW:
- I've created a simple algorithm. I was using scrapy but it was not grabbing anything. I found out that I can not scrap everything because of protection. So the links that can be extracted are very rare. However I found some that can be extracted using BeautifulSoup.
- Working on the app.py now

## FinalUpdate
- It's working now. I've used a different model. It's better now. Hopefully will work when deployed because the model is hugh. Took me time to download it. 