class Tarefas:

    def __init__(self, descricao, data, hora, status):
        self.__descricao = descricao
        self.__data = data
        self.__hora = hora
        self.__status = status

    def get_descricao(self):
        return self.__descricao

    def get_data(self):
        return self.__data

    def get_hora(self):
        return self.__hora

    def get_status(self):
        return self.__status

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_data(self, data):
        self.__data = data

    def set_hora(self, hora):
        self.__hora = hora

    def set_status(self,status):
        self.__status = status
