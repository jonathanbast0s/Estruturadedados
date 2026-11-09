from Elemento import Elemento
from NoDuplo import No
from ListaDupla import ListaDupla  # Corrigido: era ListaDE, mas a classe se chama ListaDupla

def menu():
    op = 0
    while op < 1 or op > 9:
      print("Menu:")
      print("1. Inserir no início")
      print("2. Retirar do início")
      print("3. Inserir no fim")
      print("4. Retirar do fim")
      print("5. Inserir em ordem")
      print("6. Retirar elemento")
      print("7. Imprimir lista")
      print("8. Imprimir lista inversa")
      print("9. Sair")
      op = int(input("Escolha uma opção: "))
    return op

if __name__ == '__main__':  # Corrigido: código de teste movido para bloco main para permitir importação
    l = ListaDupla()  # Corrigido: era ListaDE(), agora ListaDupla()
    op = menu()
    while op != 9:
        if op == 1:
            chave = int(input("Digite a chave: "))
            nome = input("Digite o nome: ")
            l.insereNoInicio(chave, nome)
        elif op == 2:
            no = l.retiraNoInicio()
            if no != None:
                print(f"Elemento retirado: {no.getValores()}")
            else:
                print("Lista vazia!")
        elif op == 3:
            chave = int(input("Digite a chave: "))
            nome = input("Digite o nome: ")
            l.insereNoFim(chave, nome)
        elif op == 4:
            no = l.retiraNoFim()
            if no != None:
                print(f"Elemento retirado: {no.getValores()}")
            else:
                print("Lista vazia!")
        elif op == 5:
            chave = int(input("Digite a chave: "))
            nome = input("Digite o nome: ")
            l.insereNaOrdem(chave, nome)
        elif op == 6:
            chave = int(input("Digite a chave do elemento a ser retirado: "))
            no = l.retiraNo(chave)
            if no != None:
                print(f"Elemento retirado: {no.getValores()}")
            else:
                print("Elemento não encontrado!")
        elif op == 7:
            print("Lista:")
            no = l.primeiro()
            while no != None:
                print(no.getValores())
                no = no.getProx()
        elif op == 8:
            print("Lista inversa:")
            no = l.ultimo()
            while no != None:
                print(no.getValores())
                no = no.getAnte()
        op = menu()