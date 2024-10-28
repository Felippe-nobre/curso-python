'''### `__init__`: Construtor

É o método chamado quando um objeto é criado.'''
class Livro:
    def __init__(self, titulo,autor):
        self.titulo = titulo
        self.autor = autor
'''### `__str__`: Representação em string

Define como o objeto deve ser exibido ao usar `print()`.'''
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
livro = Livro("Harry Potter", "JK Rowling")
print(livro)

'''### `__del__`: Destrutor

É chamado quando o objeto é destruído ou quando o programa termina.'''

class Livro:
    def __del__(self):
        print("Objeto Livro foi destruído")

livro = Livro()
del livro