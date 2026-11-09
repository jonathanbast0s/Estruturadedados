from ListaDupla import ListaDupla

class Fila:
    """Implementação de Fila (Queue) usando ListaDupla.

    FIFO - First In, First Out (Primeiro a entrar, primeiro a sair).
    Operações principais: enqueue (entrar na fila), dequeue (sair da fila), front (frente).
    """

    def __init__(self):
        self.__lista = ListaDupla()

    def enqueue(self, chave, nome):
        """Insere um elemento no final da fila (fim da lista)."""
        self.__lista.insereNoFim(chave, nome)

    def dequeue(self):
        """Remove e retorna o elemento da frente da fila (início da lista)."""
        no = self.__lista.retiraNoInicio()
        if no is not None:
            return no.getValores()
        return None

    def front(self):
        """Retorna o elemento da frente sem removê-lo."""
        no = self.__lista.primeiro()
        if no is not None:
            return no.getValores()
        return None

    def rear(self):
        """Retorna o elemento do fim da fila sem removê-lo."""
        no = self.__lista.ultimo()
        if no is not None:
            return no.getValores()
        return None

    def vazia(self):
        """Verifica se a fila está vazia."""
        return self.__lista.listaVazia()

    def tamanho(self):
        """Retorna o número de elementos na fila."""
        return self.__lista.tamanhoIterativo()

    def mostraFila(self):
        """Exibe todos os elementos da fila (da frente para o fim)."""
        print("Frente -> Fim:")
        self.__lista.mostraLista()

    def mostraFilaRecursivo(self):
        """Exibe a fila recursivamente."""
        self.__lista.mostraListaRecursivo()


if __name__ == "__main__":
    # Teste simples da Fila
    f = Fila()
    f.enqueue(1, "Um")
    f.enqueue(2, "Dois")
    f.enqueue(3, "Três")

    print("Fila após inserts:")
    f.mostraFila()

    print(f"\nFrente: {f.front()}")
    print(f"Fim: {f.rear()}")
    print(f"Tamanho: {f.tamanho()}")

    print("\nDesenfileirando:")
    print(f.dequeue())
    print(f.dequeue())
    print(f.dequeue())
    print(f"Vazia? {f.vazia()}")