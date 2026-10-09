import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Add it to the .env file."
    )

client = Groq(api_key=API_KEY)


def generate_response(prompt, temperature, max_tokens):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_completion_tokens=max_tokens
    )

    return response.choices[0].message.content

