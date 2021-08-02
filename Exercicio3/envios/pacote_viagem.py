class PacoteViagem:

    def __init__(self, origem, destino, duracao, custo_unitario):
        self.__origem = origem
        self.__destino = destino
        self.__duracao = duracao
        self.__custo_unitario = custo_unitario

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, origem):
        self.__origem = origem

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, destino):
        self.__destino = destino

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    @property
    def custo_unitario(self):
        return self.__custo_unitario

    @custo_unitario.setter
    def custo_unitario(self, custo_unitario):
        self.__custo_unitario = custo_unitario

