from openai import OpenAI

client = OpenAI(api_key="abcdef1234567890abcdef1234567890abcdef12")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "Explain embeddings simply"
        }
    ]
)

print(response.choices[0].message.content)