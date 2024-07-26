# definição classe Nodo
class Nodo:
    def _init_(self, numero, cor):
        self.numero = numero  # numero do cartão do paciente
        self.cor = cor  # cor do cartão do paciente
        self.proximo = None  # referência para o próximo nodo na lista encadeada


# definição classe ListaEncadeada
class listaEncadeada:
    def _init_(self):
        self.head = None  # inicializa a lista encadeada com a head vazia

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo  # se a lista estiver vazia, o novo nodo se torna a head

            return

        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = nodo  # vai inserir novo nodo no final da lista

    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return

        atual = self.head
        anterior = None

        while atual is not None and atual.cor == 'A' and atual.numero < nodo.numero:
            anterior = atual
            atual = atual.proximo

        if anterior is None:
            nodo.proximo = self.head
            self.head = nodo
        else:
            nodo.proximo = atual
            anterior.proximo = nodo

    def inserir(self):
        cor = (input('Digite a a cor do cartão (A- amarelo, V- verde:) ')).upper() #.upper converte as letras de uma string em maíuscula
        numero = int(input('Digite o número do cartão: '))

        nodo = Nodo(numero, cor)  #novo nodo

        if self.head is None:
            self.head = nodo  # se self.head estiver vazio, novo nodo se torna a head
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)  # se cor for verde, não haverá prioridade na inserção
        elif cor == 'A':
            self.inserirComPrioridade(nodo)  #se cor for amarelo, haverá prioridade

    def imprimirListaEspera(self):
        if self.head is None:
            print('Lista de espera vazia.')
            return

        atual = self.head
        while atual is not None:
            print(f"->[{atual.cor}], {atual.numero}]")  #imprime cada nodo na lista
            atual = atual.proximo

    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes para atender.")
            return

        numero_cartao = self.head.numero
        cor_cartao = self.head.cor

        self.head = self.head.proximo

        print(f"Atendendo paciente com cartão {cor_cartao} - Número {numero_cartao}")


# Função principal para o menu do sistema
def main():
    listaEspera = listaEncadeada()  #nova instância da listaEncadeada

    while True:
        print("\n===== Menu de Opções =====")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar próximo paciente")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            listaEspera.inserir()
        elif escolha == '2':
            listaEspera.imprimirListaEspera()
        elif escolha == '3':
            listaEspera.atenderPaciente()
        elif escolha == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")


if _name_ == "_main_":
    main()