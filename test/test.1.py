import os

from dotenv import load_dotenv

load_dotenv()

os.getenv("MINERU_API_TOKEN")
os.getenv("MINERU_BASE_URL")

print(os.getenv("MINERU_API_TOKEN"))
print(os.getenv("MINERU_BASE_URL"))