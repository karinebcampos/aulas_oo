class Contato:

    def __init__(self, nomecontato, emailcontato):
        self.__nomecontato = nomecontato
        self.__emailcontato = emailcontato

    def get_nomecontato(self):
        return self.__nomecontato

    def get_emailcontato(self):
        return self.__emailcontato

    def set_nomecontato(self, nome):
        self.__nomecontato = nome

    def set_emailcontato(self, emailcontato):
        self.__emailcontato = emailcontato
