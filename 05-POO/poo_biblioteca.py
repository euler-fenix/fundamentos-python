# A classe principal será chamada de "Material" e terá um construtor que recebe dois parâmetros: "titulo" e "autor_ou_editora". Essa classe também terá um método chamado "exibir_informacoes" que imprimirá na saída o título e o autor/editora do material.
# A classe "Livro" será uma subclasse da classe "Material" e terá um construtor que recebe três parâmetros: "titulo", "autor_ou_editora" e "genero". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente na classe "Material" e imprimirá o gênero do livro.
# A classe "Revista" será outra subclasse da classe "Material" e terá um construtor que recebe três parâmetros: "titulo", "autor_ou_editora" e "edicao". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente na classe "Material" e imprimirá a edição da revista.
# Crie instâncias das classes "Livro" e "Revista" com informações específicas e chame o método "exibir_informacoes" para mostrar os detalhes de cada material.

#Principal
class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor/Editora: {self.autor_ou_editora}')

#livro
class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Gênero: {self.genero}')

# revista
class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Edição: {self.edicao}')

def separador():
    print('='*60)

#instancias livro revista
livro1 = Livro('Livro Lógica de programaçao:algoritmos estruturas de dados com Python', ' André Luiz Forbellone (Autor), Bookman (Editora)', 'Programaçao')
livro2 = Livro('Python Para Desenvolvedores' ,'Luiz Eduardo Borges (Autor) NOVATEC (editora)','Programaçao')
revista1 = Revista('Revista Star wars', 'Editora Europa.', 'Ediçao 309')
revista2 = Revista('Revista Shein ', 'Editora Shha.', 'Ediçao 19')

# Exibir informacao
separador()
livro1.exibir_informacoes()
separador()
livro2.exibir_informacoes()
separador()
revista1.exibir_informacoes()
separador()
revista2.exibir_informacoes()
separador()

