from fastapi import APIRouter
from apis.routers.utils import chain,process_and_retrieval
from typing import List
import time

routers = APIRouter()

@routers.get("/")
def ping_service():
    return {"message": "Hello World"}

@routers.post("/ollama_service")
def ollama_service(document:str,description:str) -> str:
    hscode = chain.invoke({"context": document, "description": description})
    hscode = hscode.replace("\n", "").replace(" ", "")
    return hscode


@routers.post("/ollama_many_sentence")
def handle_many_input(data: List[dict]) -> List[str] :
    results = []

    start_t=time.time()
    print("len of data: ",len(data))
    for item in data:
        document = item.get("document", "")
        description = item.get("description", "")
        hscode = chain.invoke({"context": document, "description": description})
        hscode = hscode.replace("\n", "").replace(" ", "")
        results.append(hscode)
    
    print("Time to process: ",time.time()-start_t)

    return results



@routers.post("/ollama_many_sentence2")
def handle_many_input2(data: List[dict]) -> List[str] :
    results = []

    start_t=time.time()
    print("len of data: ",len(data))
    for item in data:
        document = item.get("document", "")
        description = item.get("description", "")
        hscode = chain.invoke({"context": document, "description": description})
        hscode = hscode.replace("\n", "").replace(" ", "")
        results.append(hscode)
    
    print("Time to process: ",time.time()-start_t)

    return results


@routers.post("/ollama_many_sentence3")
def handle_many_input3(data: List[dict]) -> List[str] :
    results = []

    start_t=time.time()
    print("len of data: ",len(data))
    for item in data:
        document = item.get("document", "")
        description = item.get("description", "")
        hscode = chain.invoke({"context": document, "description": description})
        hscode = hscode.replace("\n", "").replace(" ", "")
        results.append(hscode)
    
    print("Time to process: ",time.time()-start_t)

    return results


@routers.post("/ollama_many_sentence4")
def handle_many_input4(data: List[dict]) -> List[str] :
    results = []

    start_t=time.time()
    print("len of data: ",len(data))
    for item in data:
        document = item.get("document", "")
        description = item.get("description", "")
        hscode = chain.invoke({"context": document, "description": description})
        hscode = hscode.replace("\n", "").replace(" ", "")
        results.append(hscode)
    
    print("Time to process: ",time.time()-start_t)

    return results