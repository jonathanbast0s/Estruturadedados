from Elemento import Elemento
from NoDuplo import No

class ListaDpCirc:
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
            no.setAnte(no)
            self.__cabeca.setAnte(no)
            self.__cabeca.setProx(no)
        else:
            p = self.primeiro()
            u = self.ultimo()
            no.setProx(p)
            no.setAnte(u)
            p.setAnte(no)
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
            no.setAnte(None)
        else:
            p = no.getProx()
            u = self.ultimo()
            u.setProx(p)
            p.setAnte(u)
            self.__cabeca.setAnte(p)
            no.setProx(None)
            no.setAnte(None)
        return no

    def insereNoFim(self, chave, nome):
        no = self.criaNo(chave, nome)
        if self.listaVazia():
            no.setProx(no)
            no.setAnte(no)
            self.__cabeca.setAnte(no)
            self.__cabeca.setProx(no)
        else:
            p = self.primeiro()
            u = self.ultimo()
            u.setProx(no)
            no.setAnte(u)
            no.setProx(p)
            p.setAnte(no)
            self.__cabeca.setProx(no)

    def retiraNoFim(self):
        if self.listaVazia():
            return None
        no = self.ultimo()
        if self.primeiro() == self.ultimo():
            self.__cabeca.setAnte(None)
            self.__cabeca.setProx(None)
            no.setProx(None)
            no.setAnte(None)
        else:
            p = self.primeiro()
            a = no.getAnte()
            a.setProx(p)
            p.setAnte(a)
            self.__cabeca.setProx(a)
            no.setProx(None)
            no.setAnte(None)
        return no

    def insereNaOrdem(self, chave, nome):
        if self.listaVazia() or chave <= self.primeiro().getChave():
            self.insereNoInicio(chave, nome)
        elif chave >= self.ultimo().getChave():
            self.insereNoFim(chave, nome)
        else:
            no = self.criaNo(chave, nome)
            atu = self.primeiro().getProx()
            while atu != self.ultimo() and atu.getChave() < chave:
                atu = atu.getProx()
            ant = atu.getAnte()
            no.setProx(atu)
            no.setAnte(ant)
            ant.setProx(no)
            atu.setAnte(no)

    def retiraNo(self, chave):
        if self.listaVazia():
            return None
        if self.primeiro().getChave() == chave:
            return self.retiraNoInicio()
        if self.ultimo().getChave() == chave:
            return self.retiraNoFim()

        atu = self.primeiro().getProx()
        while atu != self.ultimo() and atu.getChave() != chave:
            atu = atu.getProx()

        if atu.getChave() == chave:
            ant = atu.getAnte()
            prox = atu.getProx()
            ant.setProx(prox)
            prox.setAnte(ant)
            atu.setProx(None)
            atu.setAnte(None)
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
            atu = self.ultimo()
            while True:
                print(atu.getValores())
                atu = atu.getAnte()
                if atu == self.ultimo():
                    break

    def mostraListaRecursivo(self):
        """Método público para exibir a lista em ordem direta recursivamente."""
        if self.listaVazia():
            print("Lista vazia")
        else:
            self.__mostraRecursivoAux(self.primeiro())

    def __mostraRecursivoAux(self, no):
        """Método privado auxiliar para a recursão direta."""
        print(no.getValores())
        if no.getProx() != self.primeiro():
            self.__mostraRecursivoAux(no.getProx())

    def mostraListaInversaRecursivo(self):
        """Método público para exibir a lista em ordem inversa recursivamente."""
        if self.listaVazia():
            print("Lista vazia")
        else:
            self.__mostraInversaRecursivoAux(self.ultimo())

    def __mostraInversaRecursivoAux(self, no):
        """Método privado auxiliar para a recursão inversa."""
        print(no.getValores())
        if no.getAnte() != self.ultimo():
            self.__mostraInversaRecursivoAux(no.getAnte())

    # Atividade 4: Método iterativo para retornar a quantidade de elementos
    def tamanhoIterativo(self):
        """Retorna a quantidade de elementos na lista duplamente circular (iterativo)."""
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
        """Retorna a quantidade de elementos na lista duplamente circular (recursivo)."""
        if self.listaVazia():
            return 0
        return self.__tamanhoRecursivoAux(self.primeiro())

    def __tamanhoRecursivoAux(self, no):
        """Método privado auxiliar para contar elementos recursivamente em lista duplamente circular."""
        if no.getProx() == self.primeiro():
            return 1
        return 1 + self.__tamanhoRecursivoAux(no.getProx())