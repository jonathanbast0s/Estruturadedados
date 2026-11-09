from ListaDpCirc import ListaDpCirc

class Deque:
    """Implementação de Deque (Double-ended Queue) usando ListaDpCirc.

    Um Deque (pronuncia-se "deck") é uma fila de duas extremidades que permite
    inserção e remoção de elementos tanto no início quanto no final.

    Características principais:
    - Inserção no início: O(1)
    - Inserção no final: O(1)
    - Remoção do início: O(1)
    - Remoção do final: O(1)
    - Acesso ao início: O(1)
    - Acesso ao final: O(1)
    - Pode ser usado como Pilha (LIFO) ou Fila (FIFO)

    Aplicações:
    - Verificação de palíndromos
    - Algoritmos de janela deslizante
    - Sistemas de undo/redo
    - Escalonamento de tarefas
    """

    def __init__(self):
        self.__lista = ListaDpCirc()

    # Inserções
    def insereInicio(self, chave, nome):
        """Insere um elemento no início do deque."""
        self.__lista.insereNoInicio(chave, nome)

    def insereFim(self, chave, nome):
        """Insere um elemento no final do deque."""
        self.__lista.insereNoFim(chave, nome)

    # Remoções
    def removeInicio(self):
        """Remove e retorna o elemento do início do deque."""
        no = self.__lista.retiraNoInicio()
        if no is not None:
            return no.getValores()
        return None

    def removeFim(self):
        """Remove e retorna o elemento do final do deque."""
        no = self.__lista.retiraNoFim()
        if no is not None:
            return no.getValores()
        return None

    # Acessos (sem remover)
    def getInicio(self):
        """Retorna o elemento do início sem removê-lo."""
        no = self.__lista.primeiro()
        if no is not None:
            return no.getValores()
        return None

    def getFim(self):
        """Retorna o elemento do final sem removê-lo."""
        no = self.__lista.ultimo()
        if no is not None:
            return no.getValores()
        return None

    # Verificações
    def vazia(self):
        """Verifica se o deque está vazio."""
        return self.__lista.listaVazia()

    def tamanho(self):
        """Retorna o número de elementos no deque."""
        return self.__lista.tamanhoIterativo()

    # Exibição
    def mostraDeque(self):
        """Exibe todos os elementos do deque (início -> fim)."""
        print("Início -> Fim:")
        self.__lista.mostraLista()

    def mostraDequeInverso(self):
        """Exibe todos os elementos do deque (fim -> início)."""
        print("Fim -> Início:")
        self.__lista.mostraListaInversa()

    def mostraDequeRecursivo(self):
        """Exibe o deque recursivamente (ordem direta)."""
        self.__lista.mostraListaRecursivo()

    def mostraDequeInversoRecursivo(self):
        """Exibe o deque recursivamente (ordem inversa)."""
        self.__lista.mostraListaInversaRecursivo()

    # Operações de Pilha (LIFO) - usando o início como topo
    def push(self, chave, nome):
        """Empilha (insere no início) - operação de pilha."""
        self.insereInicio(chave, nome)

    def pop(self):
        """Desempilha (remove do início) - operação de pilha."""
        return self.removeInicio()

    def top(self):
        """Retorna o topo da pilha (início) - operação de pilha."""
        return self.getInicio()

    # Operações de Fila (FIFO) - início = frente, fim = traseira
    def enqueue(self, chave, nome):
        """Enfileira (insere no fim) - operação de fila."""
        self.insereFim(chave, nome)

    def dequeue(self):
        """Desenfileira (remove do início) - operação de fila."""
        return self.removeInicio()

    def front(self):
        """Retorna a frente da fila (início) - operação de fila."""
        return self.getInicio()

    def rear(self):
        """Retorna o fim da fila (final) - operação de fila."""
        return self.getFim()


if __name__ == "__main__":
    # Teste do Deque
    print("=== TESTE DEQUE ===\n")
    d = Deque()

    print("1. Inserindo no início: 10, 20, 30")
    d.insereInicio(10, "Dez")
    d.insereInicio(20, "Vinte")
    d.insereInicio(30, "Trinta")
    d.mostraDeque()

    print("\n2. Inserindo no final: 40, 50")
    d.insereFim(40, "Quarenta")
    d.insereFim(50, "Cinquenta")
    d.mostraDeque()

    print(f"\n3. Início: {d.getInicio()}")
    print(f"   Fim: {d.getFim()}")
    print(f"   Tamanho: {d.tamanho()}")

    print("\n4. Removendo do início:")
    print(f"   Removido: {d.removeInicio()}")
    d.mostraDeque()

    print("\n5. Removendo do final:")
    print(f"   Removido: {d.removeFim()}")
    d.mostraDeque()

    print("\n6. Teste como Pilha (LIFO):")
    d2 = Deque()
    d2.push(1, "Um")
    d2.push(2, "Dois")
    d2.push(3, "Três")
    print(f"   Topo: {d2.top()}")
    print(f"   Pop: {d2.pop()}")
    print(f"   Topo após pop: {d2.top()}")

    print("\n7. Teste como Fila (FIFO):")
    d3 = Deque()
    d3.enqueue(1, "Um")
    d3.enqueue(2, "Dois")
    d3.enqueue(3, "Três")
    print(f"   Frente: {d3.front()}")
    print(f"   Dequeue: {d3.dequeue()}")
    print(f"   Nova frente: {d3.front()}")

    print("\n8. Exibição recursiva:")
    d.mostraDequeRecursivo()

    print("\n9. Exibição recursiva inversa:")
    d.mostraDequeInversoRecursivo()