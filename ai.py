from openai import OpenAI
from tokens import open
client = OpenAI(
  base_url="https://api.langdock.com/openai/eu/v1",
  api_key=open                                      # токен landgock'а из tokens.py
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "Write a short poem about cats."}
  ]
)

print(completion.choices[0].message.content)