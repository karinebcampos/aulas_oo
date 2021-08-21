class Agenda:


    def __init__(self,  nomeproprietario, ano):
        self.__nomeproprietario = nomeproprietario
        self.__ano = ano


    def get_nomeproprietatio(self):
        return self.__nomeproprietario

    def get_ano(self):
        return self.__ano

    def set_nomeproprietario(self, nomeproprietario):
        self.__nomeproprietario = nomeproprietario

    def set_ano(self, ano):
        self.__ano = ano
