class Elemento:
  """Guarda os dados de um item que pode ser armazenado na lista.

  Em uma lista duplamente encadeada, os ponteiros para o elemento anterior
  e o próximo normalmente pertencem ao nó da lista, não a esta classe.
  """
  def __init__(self, chave = 0, nome = ""):
    # A chave pode ser usada para identificar ou localizar o elemento.
    self.__chave = chave
    # O nome é o outro dado associado a este elemento.
    self.__nome = nome
  def getChave(self):
    """Retorna a chave do elemento."""
    return self.__chave
  def setChave(self, c):
    """Atualiza a chave do elemento."""
    self.__chave = c
  def getNome(self):
    """Retorna o nome do elemento."""
    return self.__nome 
  def setNome(self, n):
    """Atualiza o nome do elemento."""
    self.__nome = n 
  def getValores(self):
    """Retorna a chave e o nome, nessa ordem."""
    return self.getChave(), self.getNome()