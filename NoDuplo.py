from Elemento import Elemento 

class No:
    def __init__(self, dado=None):
        if dado is None:
            dado = Elemento()
        self.__dado = dado
        self.__prox = None # Ponteiro para o próximo nó
        self.__ante = None # Ponteiro para o nó anterior

    def getDado(self):
        return self.__dado

    def setDado(self, dado):
        self.__dado = dado

    def getProx(self):
        return self.__prox

    def setProx(self, prox):
        self.__prox = prox

    def getAnte(self):
        return self.__ante

    def setAnte(self, ante):
        self.__ante = ante

    def getChave(self):
        return self.__dado.getChave()

    def setChave(self, chave):
        self.__dado.setChave(chave)

    def getValores(self):
        return self.__dado.getValores()