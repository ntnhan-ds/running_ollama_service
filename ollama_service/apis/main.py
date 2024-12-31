# main.py
from fastapi import FastAPI
from dotenv import load_dotenv
from apis.routers.views import routers 
import os
import time

app = FastAPI()

@app.on_event("startup")
async def startup():
    load_dotenv()
    print("Ứng dụng đang khởi động...")

app.include_router(routers)  
