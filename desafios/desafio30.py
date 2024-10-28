
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descrever(self):
        return f"{self.titulo} por {self.autor}"
    
livro = Livro("Harry Potter", "JK Rowling")
print(livro.descrever())