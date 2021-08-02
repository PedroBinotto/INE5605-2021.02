class Cliente:
    def __init__(self, nome, fone, email):
        self.__nome = nome
        self.__fone = fone
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def fone(self):
        return self.__fone

    @property
    def email(self):
        return self.__email

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @fone.setter
    def fone(self, fone):
        self.__fone = fone

    @email.setter
    def email(self, email):
        self.__email = email

