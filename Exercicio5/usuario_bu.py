from abc import ABC, abstractmethod

class UsuarioBU(ABC):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf

    @property
    def dias_de_emprestimo(self):
        return self.__dias_de_emprestimo

    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, dias_de_emprestimo: int):
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        return\
"""pegou emprestado o livro: Also sprach Zarathustra com {dias_de_emprestimo} dias de prazo"""\
        .format(
            matricula = self.__matricula,
            dias_de_emprestimo = self.__dias_de_emprestimo)

    @abstractmethod
    def devolver(self, titulo_livro: str):
        return\
"""devolveu o livro: {livro}"""\
        .format(
            matricula = self.__matricula,
            livro = titulo_livro)
