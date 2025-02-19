import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def answer_question(context, question):
    """Generates an answer based on context and question using OpenAI GPT-4."""
    openai.api_key = API_KEY
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]

if __name__ == '__main__':
    context = input("Enter context: ")
    question = input("Enter question: ")
    answer = answer_question(context, question)
    print("Answer:", answer)
