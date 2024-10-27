# Definindo a exceção personalizada
class NomeCurto(Exception):
    def __init__(self, message="O nome deve ter pelo menos 5 caracteres"):
        self.message = message
        super().__init__(self.message)

# Função para verificar o nome
def verificar_nome(nome):
    if len(nome) < 5:
        raise NomeCurto
    else:
        print("Nome válido")

# Testando a função e tratando a exceção
try:
    nome = input("Digite o seu nome: ")
    verificar_nome(nome)
except NomeCurto as e:
    print(f"Erro: {e}")
