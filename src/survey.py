from dotenv import load_dotenv
from litellm import completion

load_dotenv()

reponse = completion(
    model = "mistral/mistral-tiny",
    messages = [
        {"role": "user", "content": "Antworte mit genau einer Zahl zwischen 1 und 4"}
    ]
)

print("Response:", reponse.choices[0].message.content)