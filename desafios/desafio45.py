import requests 
url = "https://jsonplaceholder.typicode.com/posts"
dados = {
    "title": "Novo Post",
    "body": "Este é o corpo do novo post.",
    "userId": 1
}
response = requests.post(url, json=dados)
print(response.status_code)
print(response.json())

