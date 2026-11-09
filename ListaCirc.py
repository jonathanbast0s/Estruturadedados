from Elemento import Elemento
from NoDuplo import No

class ListaCirc:
    def __init__(self):
        self.__cabeca = No()

    def criaNo(self, chave, nome):
        elemento = Elemento(chave, nome)
        return No(elemento)

    def primeiro(self):
        return self.__cabeca.getAnte()

    def ultimo(self):
        return self.__cabeca.getProx()

    def listaVazia(self):
        return self.primeiro() is None

    def insereNoInicio(self, chave, nome):
        no = self.criaNo(chave, nome)
        if self.listaVazia():
            no.setProx(no)
            self.__cabeca.setAnte(no)
            self.__cabeca.setProx(no)
        else:
            p = self.primeiro()
            u = self.ultimo()
            no.setProx(p)
            u.setProx(no)
            self.__cabeca.setAnte(no)

    def retiraNoInicio(self):
        if self.listaVazia():
            return None
        no = self.primeiro()
        if self.primeiro() == self.ultimo():
            self.__cabeca.setAnte(None)
            self.__cabeca.setProx(None)
            no.setProx(None)
        else:
            p = no.getProx()
            u = self.ultimo()
            u.setProx(p)
            self.__cabeca.setAnte(p)
            no.setProx(None)
        return no

    def insereNoFim(self, chave, nome):
        no = self.criaNo(chave, nome)
        if self.listaVazia():
            no.setProx(no)
            self.__cabeca.setAnte(no)
            self.__cabeca.setProx(no)
        else:
            p = self.primeiro()
            u = self.ultimo()
            u.setProx(no)
            no.setProx(p)
            self.__cabeca.setProx(no)

    def retiraNoFim(self):
        if self.listaVazia():
            return None
        no = self.ultimo()
        if self.primeiro() == self.ultimo():
            self.__cabeca.setAnte(None)
            self.__cabeca.setProx(None)
            no.setProx(None)
        else:
            p = self.primeiro()
            atu = p
            while atu.getProx() != no:
                atu = atu.getProx()
            atu.setProx(p)
            self.__cabeca.setProx(atu)
            no.setProx(None)
        return no

    def insereNaOrdem(self, chave, nome):
        if self.listaVazia() or chave <= self.primeiro().getChave():
            self.insereNoInicio(chave, nome)
        elif chave >= self.ultimo().getChave():
            self.insereNoFim(chave, nome)
        else:
            no = self.criaNo(chave, nome)
            ant = self.primeiro()
            atu = ant.getProx()
            while atu != self.ultimo() and atu.getChave() < chave:
                ant = atu
                atu = atu.getProx()
            no.setProx(atu)
            ant.setProx(no)

    def retiraNo(self, chave):
        if self.listaVazia():
            return None
        if self.primeiro().getChave() == chave:
            return self.retiraNoInicio()
        if self.ultimo().getChave() == chave:
            return self.retiraNoFim()

        ant = self.primeiro()
        atu = ant.getProx()
        while atu != self.ultimo() and atu.getChave() != chave:
            ant = atu
            atu = atu.getProx()

        if atu.getChave() == chave:
            ant.setProx(atu.getProx())
            atu.setProx(None)
            return atu
        return None

    def mostraLista(self):
        if self.listaVazia():
            print("Lista vazia")
        else:
            atu = self.primeiro()
            while True:
                print(atu.getValores())
                atu = atu.getProx()
                if atu == self.primeiro():
                    break

    def mostraListaInversa(self):
        if self.listaVazia():
            print("Lista vazia")
        else:
            elementos = []
            atu = self.primeiro()
            while True:
                elementos.append(atu.getValores())
                atu = atu.getProx()
                if atu == self.primeiro():
                    break
            for elem in reversed(elementos):
                print(elem)

    def mostraListaRecursivo(self):
        """Método público para exibir a lista circular recursivamente (ordem direta)."""
        if self.listaVazia():
            print("Lista vazia")
        else:
            self.__mostraRecursivoAux(self.primeiro())

    def __mostraRecursivoAux(self, no):
        """Método privado auxiliar para a recursão em lista circular (ordem direta)."""
        print(no.getValores())
        if no.getProx() != self.primeiro():
            self.__mostraRecursivoAux(no.getProx())

    # Atividade 3: Método recursivo para mostrar elementos em ordem inversa
    def mostraListaInversaRecursivo(self):
        """Método público para exibir a lista circular recursivamente (ordem inversa)."""
        if self.listaVazia():
            print("Lista vazia")
        else:
            # Para lista circular simples, coletamos os elementos e imprimimos inversamente
            # pois não temos ponteiro 'ante'
            self.__mostraInversaRecursivoAux(self.primeiro())

    def __mostraInversaRecursivoAux(self, no):
        """Método privado auxiliar para a recursão inversa em lista circular simples."""
        if no.getProx() != self.primeiro():
            self.__mostraInversaRecursivoAux(no.getProx())
        print(no.getValores())

    # Atividade 4: Método iterativo para retornar a quantidade de elementos
    def tamanhoIterativo(self):
        """Retorna a quantidade de elementos na lista circular (iterativo)."""
        if self.listaVazia():
            return 0
        count = 1
        atu = self.primeiro().getProx()
        while atu != self.primeiro():
            count += 1
            atu = atu.getProx()
        return count

    # Atividade 5: Método recursivo para retornar a quantidade de elementos
    def tamanhoRecursivo(self):
        """Retorna a quantidade de elementos na lista circular (recursivo)."""
        if self.listaVazia():
            return 0
        return self.__tamanhoRecursivoAux(self.primeiro())

    def __tamanhoRecursivoAux(self, no):
        """Método privado auxiliar para contar elementos recursivamente em lista circular."""
        if no.getProx() == self.primeiro():
            return 1
        return 1 + self.__tamanhoRecursivoAux(no.getProx())