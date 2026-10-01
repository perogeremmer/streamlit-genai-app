# Install library `pip install openai`

from openai import OpenAI

client = OpenAI(base_url="https://kenari.id/v1", api_key="")
r = client.chat.completions.create(
    model="deepseek-v4-1-flash",
    messages=[{"role": "user", "content": "Halo!"}],
)
print(r.choices[0].message.content)
