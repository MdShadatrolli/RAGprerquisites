import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()

# print(data)
print([item["username"] for item in data if "username" in item])
print(data[0]["email"])
print(len(data))