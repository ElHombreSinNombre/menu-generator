import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

OLLAMA_HOST = os.getenv("OLLAMA_HOST")
DATABASE_URL = os.getenv("DATABASE_URL")
CORS_ORIGIN = os.getenv("CORS_ORIGINS")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

if not OLLAMA_HOST:
    raise ValueError("OLLAMA_HOST environment variable is not set.")

origins = [origin.strip() for origin in CORS_ORIGIN.split(",")]

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
