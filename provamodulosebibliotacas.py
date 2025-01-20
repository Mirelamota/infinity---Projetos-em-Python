#Desenvolva um programa em Python que funcione como um sistema de gerenciamento de uma biblioteca. O programa deverá permitir que os usuários realizem as seguintes operações:

#Funcionalidades:
#Adicionar Livros à Biblioteca:

#O programa deve permitir que o usuário adicione novos livros à biblioteca. Para cada livro, o sistema deve armazenar:
#Título do livro
#Autor do livro
#Número de cópias disponíveis
#Listar Todos os Livros Disponíveis:

#O programa deve exibir uma lista de todos os livros disponíveis na biblioteca, incluindo o título, autor e o número de cópias disponíveis.
#Empréstimo de Livros:

#O programa deve permitir que os usuários façam o empréstimo de um livro, o que reduzirá o número de cópias disponíveis para aquele livro.
#Se não houver cópias disponíveis, o programa deve informar ao usuário que o livro não pode ser emprestado.
#Devolução de Livros:

#O programa deve permitir que os usuários devolvam livros, aumentando o número de cópias disponíveis.
#Verificar Disponibilidade de um Livro:

#O programa deve permitir que o usuário consulte se um livro específico está disponível na biblioteca, verificando o número de cópias.
#Mostrar Livros Emprestados a um Usuário Específico:

#O programa deve permitir que o usuário visualize a lista de todos os livros que ele já pegou emprestado.



class Livro:
    def __init__(self, titulo, autor, copias_disponiveis):
        self.titulo = titulo
        self.autor = autor
        self.copias_disponiveis = copias_disponiveis
        self.emprestados = 0

    def emprestar(self):
        if self.copias_disponiveis > 0:
            self.copias_disponiveis -= 1
            self.emprestados += 1
            return True
        return False

    def devolver(self):
        if self.emprestados > 0:
            self.copias_disponiveis += 1
            self.emprestados -= 1
            return True
        return False

    def verificar_disponibilidade(self):
        return self.copias_disponiveis > 0

    def __str__(self):
        return f"{self.titulo} de {self.autor} - {self.copias_disponiveis} cópias disponíveis"


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios_emprestimos = {}

    def adicionar_livro(self, titulo, autor, copias):
        livro = Livro(titulo, autor, copias)
        self.livros.append(livro)
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro disponível na biblioteca.")
        for livro in self.livros:
            print(livro)

    def emprestar_livro(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.emprestar():
                    if usuario not in self.usuarios_emprestimos:
                        self.usuarios_emprestimos[usuario] = []
                    self.usuarios_emprestimos[usuario].append(livro)
                    print(f"Livro '{titulo}' emprestado com sucesso!")
                    return
                else:
                    print(f"Não há cópias disponíveis de '{titulo}' para empréstimo.")
                    return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

    def devolver_livro(self, titulo, usuario):
        if usuario in self.usuarios_emprestimos:
            for livro in self.usuarios_emprestimos[usuario]:
                if livro.titulo == titulo:
                    if livro.devolver():
                        self.usuarios_emprestimos[usuario].remove(livro)
                        print(f"Livro '{titulo}' devolvido com sucesso!")
                        return
                    else:
                        print(f"Erro ao devolver o livro '{titulo}'.")
                        return
            print(f"O usuário '{usuario}' não possui o livro '{titulo}' emprestado.")
        else:
            print(f"O usuário '{usuario}' não possui empréstimos.")

    def verificar_disponibilidade_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.verificar_disponibilidade():
                    print(f"O livro '{titulo}' está disponível para empréstimo.")
                else:
                    print(f"O livro '{titulo}' não está disponível no momento.")
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

    def listar_livros_emprestados_usuario(self, usuario):
        if usuario in self.usuarios_emprestimos:
            emprestados = self.usuarios_emprestimos[usuario]
            if emprestados:
                print(f"Livros emprestados por '{usuario}':")
                for livro in emprestados:
                    print(f"- {livro.titulo} de {livro.autor}")
            else:
                print(f"O usuário '{usuario}' não possui livros emprestados.")
        else:
            print(f"O usuário '{usuario}' não possui empréstimos.")



biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 5)
biblioteca.adicionar_livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 3)
biblioteca.adicionar_livro("O Código Da Vinci", "Dan Brown", 2)

# Listando livros disponiveis
print("\nLivros disponíveis:")
biblioteca.listar_livros()

# Empréstimo de um livro
biblioteca.emprestar_livro("O Senhor dos Anéis", "João")
biblioteca.emprestar_livro("Harry Potter e a Pedra Filosofal", "Maria")

# Listando livros emprestados por Joao
print("\nLivros emprestados por Joao:")
biblioteca.listar_livros_emprestados_usuario("João")

# Verificando disponibilidade de um livro
print("\nVerificando disponibilidade do livro 'O Código Da Vinci':")
biblioteca.verificar_disponibilidade_livro("O Código Da Vinci")

# Devolvendo um livro
biblioteca.devolver_livro("O Senhor dos Anéis", "João")

# Listando livros emprestados por João novamente
print("\nLivros emprestados por João após devolução:")
biblioteca.listar_livros_emprestados_usuario("João")

# Listando livros disponíveis após devolução
print("\nLivros disponíveis após devolução:")
biblioteca.listar_livros()
