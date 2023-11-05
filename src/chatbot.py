import openai
from decouple import config

openai.api_key =  config("OPENAI_API_KEY")

messages = [{"role":"system", "content":"You are a helpfull coding assistant, who gives very short and compact answers."},]

while True:
  message = input("User: ")
  if message:
    messages.append(
      {"role": "user", "content": message}
    )
    chat = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", messages=messages
    )
  reply = chat.choices[0].message.content
  print(f"ChatGPT: {reply}")
  messages.append({"role":"assistant", "content": reply})
