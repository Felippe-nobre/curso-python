import requests
url = ("https://jsonplaceholder.typicode.com/posts/1")
dados = {
    "title": "Título Atualizado",
    "body": "Este é o corpo atualizado do post.",
    "userId": 1
}
response = requests.put(url, json=dados)
print("Status Code: ",response.status_code)
print("Resposta json: ",response.json())