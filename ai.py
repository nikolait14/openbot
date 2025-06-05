from openai import OpenAI
from tokens import open


client = OpenAI(
  base_url="https://api.langdock.com/openai/eu/v1",
  api_key=open                                      # токен landgock'а из tokens.py
)


def request(req, model):
    completion = client.chat.completions.create(
      model=model,
      messages=[
        {f"role": "user", "content": {req}}
      ]
    )

    print(completion.choices[0].message.content)
