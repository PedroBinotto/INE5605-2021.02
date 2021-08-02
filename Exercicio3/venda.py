

class Venda:
	def __init__(
			self, codigo: int,
			cliente: Cliente,
			descricao: str,
			pacote: PacoteViagem,
			quantidade: int
		):
    """Insira aqui todos metodos e atributos ... """
		self.__codigo = codido
		self.__cliente = cliente
		self.__descricao = descricao
		self.__pacote = pacote
		self.__quantidade = quantidade
	
	@property
	def codigo(self):
		return self.__codigo

	@codigo.setter
	def codigo(self, codigo)
		return self.__codigo

	@property
	def cliente(self):
		return self.__cliente

	@cliente.setter
	def cliente(self, cliente)
		return self.__cliente

	@property
	def descricao(self):
		return self.__descricao

	@descricao.setter
	def descricao(self, descricao)
		return self.__descricao

	@property
	def pacote(self):
		return self.__pacote

	@pacote.setter
	def pacote(self, pacote)
		return self.__pacote

	@property
	def quantidade(self):
		return self.__quantidade

	@quantidade.setter
	def quantidade(self, quantidade)
		return self.__quantidade

	def preco_total(self):
		return self.__pacote.custo_unitario * self.__quantidade

