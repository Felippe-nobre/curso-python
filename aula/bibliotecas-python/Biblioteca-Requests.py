'''# Biblioteca Requests (requisições HTTP)

A **Requests** é uma biblioteca popular em Python que permite fazer requisições HTTP de forma simples e eficiente. Ela é amplamente utilizada para interagir com APIs, baixar conteúdo da web e realizar operações de web scraping.'''

import requests as req

#Fazendo requisições HTTP
#A requisição GET é usada para obter dados de uma URL. É a forma mais comum de requisição HTTP
response = req.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json)

#Requisição POST
#A requisição POST é usada para enviar dados para um servidor.
url = "https://jsonplaceholder.typicode.com/posts"
dados = {
    "title": "Aprendendo Requests",
    "body": "A biblioteca Requests é muito útil!",
    "userId": 1
}
response = req.post(url, json=dados)
print(response.status_code)
print(response.json)

'''## Principais métodos HTTP

Além de `GET` e `POST`, Requests também suporta outros métodos HTTP, como:

- **PUT**: Usado para atualizar dados em um servidor.
- **DELETE**: Usado para excluir dados em um servidor.'''

# Exemplo de requisição PUT
response_put = req.put("<https://jsonplaceholder.typicode.com/posts/1>", json={"title": "Novo título"})
print(response_put.status_code)

# Exemplo de requisição DELETE
response_delete = req.delete("<https://jsonplaceholder.typicode.com/posts/1>")
print(response_delete.status_code)

## Trabalhando com parâmetros e cabeçalhos

#Você pode passar **parâmetros** e **cabeçalhos** nas requisições para obter resultados específicos ou enviar informações adicionais.'''

#Passando parâmetros em uma requisição GET
params = {"userId": 1}
response = req.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(response.json())

#Passando cabeçalhos em uma requisição
headers = {"Authorization": "Bearer seu_token"}
response = req.get("https://api.exemplo.com/dados", headers=headers)
print(response.status_code)


'''## Tratamento de erros e exceções

É importante sempre verificar o status da resposta e tratar possíveis erros.'''

try:
    response = req.get("https://jsonplaceholder.typicode.com/todos/1")
    response.raise_for_status()
    dados = response.json()
    print(dados)
except req.exceptions.HTTPError as err:
    print(f"Erro HTTP: {err}")
except req.exceptions.RequestException as err:
    print(f"Erro de requisição: {err}")