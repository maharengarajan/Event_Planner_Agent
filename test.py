from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key=GROQ_API_KEY, model="Llama-3.3-70b-Versatile")
print(llm.invoke("Hi").content)
