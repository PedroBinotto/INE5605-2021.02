from abc import abstractmethod
from usuario_bu import UsuarioBU


class Funcionario(UsuarioBU):
    @abstractmethod
    def __init__(
        self,
        departamento: str,
        cpf: int,
        dias_de_emprestimo: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo
        if isinstance(departamento, str):
            self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento: str):
        if isinstance(departamento, str):
            self.__departamento = departamento

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        return\
"""do departamento "{departamento}" pegou emprestado o livro: Also sprach Zarathustra com {dias_de_emprestimo} dias de prazo"""\
        .format(
            departamento = self.__departamento,
            dias_de_emprestimo = self.__dias_de_emprestimo)

    @abstractmethod
    def devolver(self, titulo_livro: str):
        return\
"""do departamento "{departamento}" devolveu o livro: {livro}"""\
        .format(
            departamento = self.__departamento,
            dias_de_emprestimo = self.__dias_de_emprestimo)

