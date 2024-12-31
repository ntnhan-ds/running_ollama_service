import pandas as pd 
import bm25s
from tqdm import tqdm
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.docstore.document import Document
import torch
from langchain_ollama.llms import OllamaLLM
from langchain.docstore.document import Document
import os
from concurrent.futures import ThreadPoolExecutor
import re
import time

prompt = ChatPromptTemplate.from_messages([
        HumanMessagePromptTemplate.from_template(
        f"""
        Extract the appropriate 6-digit HS Code base on the product description and retrieved document by thoroughly analyzing its details and utilizing a reliable and up-to-date HS Code database for accurate results.
        Only return the HS Code as a 6-digit number .
        Example: 123456
        Context: {{context}}
        Description: {{description}}
        Answer:

        """
        )
    ])
    

device = "cuda" if torch.cuda.is_available() else "cpu"

llm = OllamaLLM(model="gemma2:9b-instruct-q4_0", temperature=0, device=device,num_thread=16)
chain = prompt|llm
def process_and_retrieval(documents,des):

    hscode = chain.invoke({"context": documents, "description": des})
    hscode = hscode.replace("\n", "").replace(" ", "")
    return hscode
