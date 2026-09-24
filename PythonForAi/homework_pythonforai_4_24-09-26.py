import time
from tenacity import retry, stop_after_attempt, wait_exponential
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from requests import ReadTimeout

#task 1
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
#
# client = genai.Client(api_key=api_key)
#
# def get_gemini_response(prompt):
#     time.sleep(0.3)
#     response = client.models.generate_content(
#         model="gemini-3.6-flash",
#         contents=[prompt],
#     )
#     return response.text
#
# response = get_gemini_response("How are you doing?")
# print(response)

#task 2

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
#
# timeout_seconds = 10
# client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=timeout_seconds * 1000))
#
# def get_gemini_response(prompt):
#     time.sleep(0.3)
#     try:
#         response = client.models.generate_content(
#             model="gemini-3.6-flash",
#             contents=[prompt]
#         )
#         return response.text
#     except ReadTimeout:
#         return f"Превышен таймаут ({timeout_seconds} секунд)."
#     except Exception as e:
#         return f"Ошибка: {str(e)}"
#
#
#
# response = get_gemini_response("How are you doing?")
# if response:
#     print(response)
# else:
#     print("Нет ответа")

#task 3

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

timeout_seconds = 10
client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=timeout_seconds * 1000))

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def get_gemini_response(prompt):
    time.sleep(0.3)
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=[prompt]
        )
        return response.text
    except ReadTimeout:
        return f"Превышен таймаут ({timeout_seconds} секунд)."
    except Exception as e:
        return f"Ошибка: {str(e)}"

response = get_gemini_response("How are you doing?")
if response:
    print(response)
else:
    print("Нет ответа")