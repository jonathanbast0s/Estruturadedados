from Elemento import Elemento
from NoDuplo import No

class ListaDupla:
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
            self.__cabeca.setAnte(no)
            self.__cabeca.setProx(no)
        else:
            p = self.primeiro()
            no.setProx(p)
            p.setAnte(no)
            self.__cabeca.setAnte(no)

    def retiraNoInicio(self):
        if self.listaVazia():
            return None
        no = self.primeiro()
        prox = no.getProx()
        if prox is None:
            self.__cabeca.setAnte(None)
            self.__cabeca.setProx(None)
        else:
            prox.setAnte(None)
            self.__cabeca.setAnte(prox)
            no.setProx(None)
        return no

    def insereNoFim(self, chave, nome):
        no = self.criaNo(chave, nome)
        if self.listaVazia():
            self.__cabeca.setAnte(no)
            self.__cabeca.setProx(no)
        else:
            u = self.ultimo()
            u.setProx(no)
            no.setAnte(u)
            self.__cabeca.setProx(no)

    def retiraNoFim(self):
        if self.listaVazia():
            return None
        no = self.ultimo()
        ante = no.getAnte()
        if ante is None:
            self.__cabeca.setAnte(None)
            self.__cabeca.setProx(None)
        else:
            ante.setProx(None)
            self.__cabeca.setProx(ante)
            no.setAnte(None)
        return no

    def insereNaOrdem(self, chave, nome):
        no = self.criaNo(chave, nome)
        if self.listaVazia():
            self.__cabeca.setAnte(no)
            self.__cabeca.setProx(no)
        else:
            ant = None
            atu = self.primeiro()
            while atu is not None and atu.getChave() < chave:
                ant = atu
                atu = atu.getProx()

            if ant is None:
                no.setProx(atu)
                atu.setAnte(no)
                self.__cabeca.setAnte(no)
            elif atu is None:
                no.setAnte(ant)
                ant.setProx(no)
                self.__cabeca.setProx(no)
            else:
                no.setProx(atu)
                no.setAnte(ant)
                ant.setProx(no)
                atu.setAnte(no)

    def retiraNo(self, chave):
        if self.listaVazia():
            return None
        atu = self.primeiro()
        while atu is not None and atu.getChave() != chave:
            atu = atu.getProx()
        
        if atu is None:
            return None

        ant = atu.getAnte()
        prox = atu.getProx()

        if ant is None and prox is None:
            self.__cabeca.setAnte(None)
            self.__cabeca.setProx(None)
        elif ant is None:
            self.__cabeca.setAnte(prox)
            prox.setAnte(None)
        elif prox is None:
            self.__cabeca.setProx(ant)
            ant.setProx(None)
        else:
            ant.setProx(prox)
            prox.setAnte(ant)

        atu.setProx(None)
        atu.setAnte(None)
        return atu

    def mostraLista(self):
        if self.listaVazia():
            print("Lista vazia")
        else:
            atu = self.primeiro()
            while atu is not None:
                print(atu.getValores())
                atu = atu.getProx()

    def mostraListaInversa(self):
        if self.listaVazia():
            print("Lista vazia")
        else:
            atu = self.ultimo()
            while atu is not None:
                print(atu.getValores())
                atu = atu.getAnte()
                
    def mostraListaRecursivo(self):
        """Método público para exibir a lista recursivamente (ordem direta)."""
        if self.listaVazia():
            print("Lista vazia")
        else:
            self.__mostraRecursivoAux(self.primeiro())

    def __mostraRecursivoAux(self, no):
        """Método privado auxiliar para a recursão (ordem direta)."""
        if no is not None:
            print(no.getValores())
            self.__mostraRecursivoAux(no.getProx())

    # Atividade 3: Método recursivo para mostrar elementos em ordem inversa
    def mostraListaInversaRecursivo(self):
        """Método público para exibir a lista recursivamente (ordem inversa)."""
        if self.listaVazia():
            print("Lista vazia")
        else:
            self.__mostraInversaRecursivoAux(self.ultimo())

    def __mostraInversaRecursivoAux(self, no):
        """Método privado auxiliar para a recursão inversa."""
        if no is not None:
            print(no.getValores())
            self.__mostraInversaRecursivoAux(no.getAnte())

    # Atividade 4: Método iterativo para retornar a quantidade de elementos
    def tamanhoIterativo(self):
        """Retorna a quantidade de elementos na lista (iterativo)."""
        count = 0
        atu = self.primeiro()
        while atu is not None:
            count += 1
            atu = atu.getProx()
        return count

    # Atividade 5: Método recursivo para retornar a quantidade de elementos
    def tamanhoRecursivo(self):
        """Retorna a quantidade de elementos na lista (recursivo)."""
        return self.__tamanhoRecursivoAux(self.primeiro())

    def __tamanhoRecursivoAux(self, no):
        """Método privado auxiliar para contar elementos recursivamente."""
        if no is None:
            return 0
        return 1 + self.__tamanhoRecursivoAux(no.getProx())