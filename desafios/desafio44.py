import requests as req
response = req.get("https://jsonplaceholder.typicode.com/users")
if response.status_code == 200:
    dados = response.json()
    for dado in dados:
        print(f"Nome: {dado['name']}")
        print(f"Email: {dado['email']}")
        print("---------------------------")
else:
    print(f"Erro. Código de resposta: ", response.status_code)