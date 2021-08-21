class Menu:

    def __init__(self, cadastrarcontato, listarcontato, excluircontato, criartarefa, listartarefa, excluirtarefa):
        self.__cadastrarcontato = cadastrarcontato
        self.__listarcontato = listarcontato
        self.__excluircontato = excluircontato
        self.__criartarefa = criartarefa
        self.__listartarefa = listartarefa
        self.__excluirtarefa = excluirtarefa

    def get_cadastrocontato(self):
        return self.__cadastrarcontato

    def get_listarcontato(self):
        return self.__listarcontato

    def get_excluircontato(self):
        return self.__excluircontato

    def get_criartarefa(self):
        return self.__criartarefa

    def get_listartarefa(self):
        return self.__listartarefa

    def get_excluirtarefa(self):
        return self.__excluirtarefa
