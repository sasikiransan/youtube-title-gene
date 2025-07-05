import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

def generate_metadata(script):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    prompt = (
        "You are a YouTube content optimizer.\n"
        "Generate a catchy video title and SEO-optimized video description "
        "(with CTAs, hashtags) for the following script:\n\n"
        f"{script}\n\n"
        "Output in this format:\n"
        "Title: ...\n"
        "Description: ..."
    )

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    content = response.json()['choices'][0]['message']['content']

    try:
        title = content.split("Title:")[1].split("Description:")[0].strip()
        description = content.split("Description:")[1].strip()
        return title, description
    except:
        return "⚠️ Title parsing failed", "⚠️ Description parsing failed"
