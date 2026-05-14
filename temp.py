import requests

data = {
    "name": "Shadat",
    "course": "RAG"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.json())

print(data)