import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if response.status_code == 200:
    data = response.json()
    print("Título: ", data["title"])
else:
    print("Erro. Código de resposta: ", response.status_code)
