from funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, departamento: str, cpf: int):
        if isinstance(departamento, str):
            self.__departamento = departamento
        if isinstance(cpf, int):
            self.__cpf = cpf
        self.__dias_de_emprestimo = 20

    def emprestar(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            return\
"""Professor do departamento "{departamento}" pegou emprestado o livro: {livro} com {dias_de_emprestimo} dias de prazo"""\
            .format(departamento = self.__departamento,
                livro = titulo_livro,
                dias_de_emprestimo = self.__dias_de_emprestimo)

    def devolver(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            return\
"""Professor do departamento "{departamento}" devolveu o livro: {livro}"""\
            .format(
                departamento = self.__departamento,
                livro = titulo_livro)
