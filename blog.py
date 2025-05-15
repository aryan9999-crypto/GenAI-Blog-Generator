# blog.py — Generate a Blog with Hugging Face Inference API 📝

import os
import requests
from dotenv import load_dotenv

# 1. Load your HF token from .env (HF_API_KEY=hf_…)
load_dotenv()
API_KEY = os.getenv("API_KEY")



# 2. Point at the smaller FLAN-T5 base model (<1 GB)
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
headers = {"Authorization": f"Bearer {API_KEY}"}

def generate_blog(paragraph_topic: str) -> str:
    prompt = (
        f"Write an informative and detailed article of approximately 200 words about {paragraph_topic}. "
        "Include specific examples, elaborate on key points, and ensure the content is comprehensive and non-repetitive."
    )
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 800,
            "temperature": 0.7,
            "top_p": 0.8,
            "repetition_penalty": 1.3,
            "do_sample": True
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code != 200:
            return f"API Error [{response.status_code}]: {response.text}"
        # The API returns a list; take the first generation
        return response.json()[0]["generated_text"]
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while input("Write a paragraph? Y for yes, anything else for no: ").strip().upper() == "Y":
        topic = input("What should this paragraph talk about? ").strip()
        print("\n" + generate_blog(topic) + "\n")


