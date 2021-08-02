from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        cnt = 0
        if isinstance(tipo, TipoChamado):
            for chamado in self.__chamados:
                if chamado.tipo.codigo == tipo.codigo:
                    cnt += 1
        return cnt

    def inclui_chamado(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado) -> Chamado:

        if not (isinstance(data, Date) and\
                isinstance(cliente, Cliente) and\
                isinstance(tecnico, Tecnico) and\
                isinstance(tipo, TipoChamado)):
            return None

        for chamado in self.__chamados:
            if chamado.data == data and\
                chamado.cliente.codigo == cliente.codigo and\
                chamado.tecnico.codigo == tecnico.codigo and\
                chamado.tipo.codigo == tipo.codigo:
                return None

        chamado = Chamado(
            data = data,
            cliente = cliente,
            tecnico = tecnico,
            titulo = titulo,
            descricao = descricao,
            prioridade = prioridade,
            tipo = tipo)
        self.__chamados.append(chamado)
        return chamado

    def inclui_tipochamado(
        self,
        codigo: int,
        nome: str,
        descricao: str) -> TipoChamado:
        for tipo in self.__tipos_chamados:
            if tipo.codigo == codigo:
                return None
        tipo = TipoChamado(
            codigo = codigo,
            descricao = descricao,
            nome = nome)
        self.__tipos_chamados.append(tipo)
        return tipo

    def print_tipos(self):
        for tipo in self.__tipos_chamados:
            print(tipo.nome)

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados
