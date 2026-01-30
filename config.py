import os
from dotenv import load_dotenv

load_dotenv()  # load file .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4o-mini"
LANGS = ["vi"]
