from abc import abstractmethod
from usuario_bu import UsuarioBU


class Aluno(UsuarioBU):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo
        if isinstance(matricula, int):
            self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        if isinstance(matricula, int):
            self.__matricula = matricula

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        return\
"""Aluno de matricula "{matricula}" pegou emprestado o livro: Also sprach Zarathustra com {dias_de_emprestimo} dias de prazo"""\
        .format(
            matricula = self.__matricula,
            dias_de_emprestimo = self.__dias_de_emprestimo)

    @abstractmethod
    def devolver(self, titulo_livro: str):
        return\
"""Aluno de matricula "{matricula}" devolveu o livro: {livro}"""\
        .format(
            matricula = self.__matricula,
            livro = titulo_livro)
