#task 1
from google import genai
from dotenv import load_dotenv
import os
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
#client = genai.Client(api_key="...")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=["What the best trainings plan for teen in bodybuilding?"]
)

print(response.text)

#task 2

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=["What the best trainings plan for teen in bodybuilding?"]
)

print(response.text)
