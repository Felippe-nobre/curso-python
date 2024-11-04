import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)
print("Status Code: ",response.status_code)
if response.status_code == 200 or response.status_code == 204:
    print("O recurso foi excluído com sucesso.")
else:
    print("Falha ao excluir o recurso.")