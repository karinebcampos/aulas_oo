from agenda import Agenda
from contato import Contato
from tarefas import Tarefas


class Main:


    def __init__(self):
        self.__contatos = []
        self.__tarefas = []
        self.__agenda = []


    def criar_contato(self):
        nome = input('Digite o nome do contato: ')
        email = input('Digite o email do contato: ')
        contato = Contato(nome, email)
        self.__contatos.append(contato)

    def listar_contato(self):
        for id, contato in enumerate(self.__contatos):
            print(str(id) + 'nome ' + contato.get_nomecontato() +
                  'email' + contato.get_emailcontato())


    def excluir_contato(self):
        id = input('Digite o numero do id do contato que deseja excluir: ')
        self.__contatos.pop(int(id))
        print('Contato excluído')


    def criar_tarefa(self):
        descricao = input('Digite uma descricao para tarefa: ')
        data = input('Digite a data da tarefa: ')
        hora = input('Digite a hora da tarefa: ')
        status = input('Digite o status da tarefa: ')
        tarefas = Tarefas(descricao, data, hora, status)
        self.__tarefas.append(tarefas)


    def listar_tarefas(self):
        for id, tarefas in enumerate(self.__tarefas):
            print(str(id) + 'descricao ' + tarefas.get_descricao() +
                  'data ' + tarefas.get_data() + 'hora ' + tarefas.get_hora() +
                  'status ' + tarefas.get_status())


    def excluir_tarefa(self):
        id = input('Digite o número do id da tarefa que deseja excluir: ')
        self.__tarefas.pop(int(id))
        print('Tarefa excluída')

    def agenda_ano(self):
        nomeproprietario = input('Informe o nome do proprietário da agenda: ')
        ano = input('Informe o ano da agenda: ')
        agenda = Agenda(nomeproprietario, ano)
        self.__agenda.append(agenda)

    def menu(self):
        print('1 informe o nome do proprietário da agenda e o ano: ')
        print('2 Cadastro de contato : ')
        print('3 Listar contato : ')
        print('4 Excluir contato : ')
        print('5 Criar tarefa : ')
        print('6 Listar tarefa : ')
        print('7 Excluir tarefa : ')


    def executar(self):
        while True:
            self.menu()
            opcao = input('Digite a opção desejada: ')
            print(opcao)
            if opcao == '1':
                self.agenda_ano()
            elif opcao == '2':
                self.criar_contato()
            elif opcao == '3':
                self.listar_contato()
            elif opcao == '4':
                self.excluir_contato()
            elif opcao == '5':
                self.criar_tarefa()
            elif opcao == '6':
                self.listar_tarefas()
            elif opcao == '7':
                self.excluir_tarefa()




Main().executar()

