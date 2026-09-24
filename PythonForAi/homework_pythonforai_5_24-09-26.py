import os
import sys
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

#task 1

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

promt = ChatPromptTemplate.from_template("Напишите краткий текст на русском языке (3-5 предложений):\n\n{context}")

def summarize_url(url, ai):
    if ai is None:
        ai = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key=api_key)
    docs = WebBaseLoader(url).load()
    chain = create_stuff_documents_chain(ai, promt)
    return chain.invoke({"context": docs})


url = sys.argv[1] if len(sys.argv) > 1 else "https://habr.com/ru/articles/883604/"
print(url)
print(summarize_url(url))

