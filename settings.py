from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage


load_dotenv()

os.environ["LANGSMITH_TRACING"] = "true"

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

if __name__ == "__main__":
    print("Model initialized successfully.")
    res = model.invoke([HumanMessage(content="Hi! I'm Bob")])
    print(res)