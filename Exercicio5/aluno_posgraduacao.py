from aluno import Aluno

class AlunoPosGraduacao(Aluno):
    def __init__(
        self,
        cpf: int,
        dias_de_emprestimo: int,
        matricula: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo
        if isinstance(matricula, int):
            self.__matricula = matricula
        self.__elaborando_tese = False

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese: bool):
        if isinstance(elaborando_tese, bool):
            self.__elaborando_tese = elaborando_tese

    def emprestar(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            return\
"""Aluno de matricula "{matricula}" pegou emprestado o livro: {livro} com {dias_de_emprestimo} dias de prazo"""\
            .format(
                matricula = self.__matricula,
                livro = titulo_livro,
                dias_de_emprestimo = (self.__dias_de_emprestimo * 2)\
                    if self.__elaborando_tese == True\
                    else self.__dias_de_emprestimo)

    def devolver(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            return\
"""Aluno de matricula "{matricula}" devolveu o livro: {livro}"""\
            .format(matricula = self.__matricula, livro = titulo_livro)
