import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

def generate_summary(content, query=""):
    prompt = f"""
    You are an AI assistant. Use the given context to either summarize or answer the question.

    Context:
    {content}

    Question: {query if query else 'Summarize the given content'}
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": prompt}],
            temperature=0.7,
            max_tokens=512,
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Error generating response."
