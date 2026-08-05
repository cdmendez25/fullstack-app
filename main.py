import os
from supabase import create_client, Client
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Succesfully Conected to Supabase"}