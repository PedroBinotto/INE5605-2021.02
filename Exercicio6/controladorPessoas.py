from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(
        self,
        codigo :int,
        nome :str) -> Cliente:
        cliente = Cliente(nome=nome, codigo=codigo)
        for cliente in self.__clientes:
           if cliente.codigo == codigo:
               return None
        self.__clientes.append(cliente)
        return cliente

    def inclui_tecnico(
        self,
        codigo :int,
        nome :str) -> Tecnico:
        tecnico = Tecnico(nome=nome, codigo=codigo)
        for tecnico in self.__tecnicos:
           if tecnico.codigo == codigo:
               return None
        self.__tecnicos.append(tecnico)
        return tecnico


