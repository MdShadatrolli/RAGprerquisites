from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

completion = client.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[
        {
            "role": "user",
            "content": "Explain embeddings in simple words"
        }
    ],
    temperature=0,
    max_tokens=200,
    stream=True
)

for chunk in completion:

    if not chunk.choices:
        continue

    delta = chunk.choices[0].delta.content

    if delta:
        print(delta, end="")