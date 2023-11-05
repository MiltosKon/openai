from decouple import config
import requests as re
import json


my_key = config("OPENAI_API_KEY")
URL = "https://api.openai.com/v1/chat/completions"

payload = {
"model": "gpt-3.5-turbo",
"messages": [{"role":"user", "content": f"List popular coding languages"},],
"temperature" : 1.0,
}

headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {my_key}"
}

response = re.post(URL, headers=headers, json=payload, stream=False)

byte_str = response.content
json_string = byte_str.decode('utf-8')
json_data = json.loads(json_string)

print(json_data["choices"][0]["message"]["content"])