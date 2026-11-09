from ListaDupla import ListaDupla

class Pilha:
    """Implementação de Pilha (Stack) usando ListaDupla.

    LIFO - Last In, First Out (Último a entrar, primeiro a sair).
    Operações principais: push (empilhar), pop (desempilhar), top (topo).
    """

    def __init__(self):
        self.__lista = ListaDupla()

    def push(self, chave, nome):
        """Insere um elemento no topo da pilha (início da lista)."""
        self.__lista.insereNoInicio(chave, nome)

    def pop(self):
        """Remove e retorna o elemento do topo da pilha."""
        no = self.__lista.retiraNoInicio()
        if no is not None:
            return no.getValores()
        return None

    def top(self):
        """Retorna o elemento do topo sem removê-lo."""
        no = self.__lista.primeiro()
        if no is not None:
            return no.getValores()
        return None

    def vazia(self):
        """Verifica se a pilha está vazia."""
        return self.__lista.listaVazia()

    def tamanho(self):
        """Retorna o número de elementos na pilha."""
        return self.__lista.tamanhoIterativo()

    def mostraPilha(self):
        """Exibe todos os elementos da pilha (do topo para a base)."""
        print("Topo -> Base:")
        self.__lista.mostraLista()

    def mostraPilhaRecursivo(self):
        """Exibe a pilha recursivamente."""
        self.__lista.mostraListaRecursivo()


if __name__ == "__main__":
    # Teste simples da Pilha
    p = Pilha()
    p.push(1, "Um")
    p.push(2, "Dois")
    p.push(3, "Três")

    print("Pilha após inserts:")
    p.mostraPilha()

    print(f"\nTopo: {p.top()}")
    print(f"Tamanho: {p.tamanho()}")

    print("\nDesempilhando:")
    print(p.pop())
    print(p.pop())
    print(p.pop())
    print(f"Vazia? {p.vazia()}")