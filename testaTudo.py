#!/usr/bin/env python3
"""Teste completo de todas as implementações das atividades."""

from ListaDupla import ListaDupla
from ListaCirc import ListaCirc
from ListaDpCirc import ListaDpCirc
from Pilha import Pilha
from Fila import Fila
from Deque import Deque

def testar_lista_dupla():
    print("=" * 60)
    print("TESTE: ListaDupla")
    print("=" * 60)

    l = ListaDupla()

    # Inserções
    print("\n1. Inserindo elementos:")
    l.insereNoInicio(3, "Três")
    l.insereNoInicio(2, "Dois")
    l.insereNoInicio(1, "Um")
    l.insereNoFim(4, "Quatro")
    l.insereNoFim(5, "Cinco")

    print("Lista (iterativo):")
    l.mostraLista()

    print("\nLista inversa (iterativo):")
    l.mostraListaInversa()

    # Atividade 2: Recursivo ordem direta
    print("\n2. Mostra recursiva (ordem direta):")
    l.mostraListaRecursivo()

    # Atividade 3: Recursivo ordem inversa
    print("\n3. Mostra recursiva (ordem inversa):")
    l.mostraListaInversaRecursivo()

    # Atividade 4: Tamanho iterativo
    print(f"\n4. Tamanho iterativo: {l.tamanhoIterativo()}")

    # Atividade 5: Tamanho recursivo
    print(f"5. Tamanho recursivo: {l.tamanhoRecursivo()}")

    # Testar remoções
    print("\n6. Removendo do início:")
    print(l.retiraNoInicio().getValores())
    l.mostraLista()

    print("\n7. Removendo do fim:")
    print(l.retiraNoFim().getValores())
    l.mostraLista()

    print("\n8. Testando lista vazia:")
    l2 = ListaDupla()
    l2.mostraListaRecursivo()
    l2.mostraListaInversaRecursivo()
    print(f"Tamanho iterativo vazio: {l2.tamanhoIterativo()}")
    print(f"Tamanho recursivo vazio: {l2.tamanhoRecursivo()}")

def testar_lista_circ():
    print("\n" + "=" * 60)
    print("TESTE: ListaCirc (Circular Simples)")
    print("=" * 60)

    l = ListaCirc()

    print("\n1. Inserindo elementos:")
    l.insereNoInicio(3, "Três")
    l.insereNoInicio(2, "Dois")
    l.insereNoInicio(1, "Um")
    l.insereNoFim(4, "Quatro")
    l.insereNoFim(5, "Cinco")

    print("Lista (iterativo):")
    l.mostraLista()

    print("\nLista inversa (iterativo - usando array):")
    l.mostraListaInversa()

    # Atividade 2: Recursivo ordem direta
    print("\n2. Mostra recursiva (ordem direta):")
    l.mostraListaRecursivo()

    # Atividade 3: Recursivo ordem inversa
    print("\n3. Mostra recursiva (ordem inversa):")
    l.mostraListaInversaRecursivo()

    # Atividade 4: Tamanho iterativo
    print(f"\n4. Tamanho iterativo: {l.tamanhoIterativo()}")

    # Atividade 5: Tamanho recursivo
    print(f"5. Tamanho recursivo: {l.tamanhoRecursivo()}")

    print("\n6. Testando lista vazia:")
    l2 = ListaCirc()
    l2.mostraListaRecursivo()
    l2.mostraListaInversaRecursivo()
    print(f"Tamanho iterativo vazio: {l2.tamanhoIterativo()}")
    print(f"Tamanho recursivo vazio: {l2.tamanhoRecursivo()}")

def testar_lista_dp_circ():
    print("\n" + "=" * 60)
    print("TESTE: ListaDpCirc (Duplamente Circular)")
    print("=" * 60)

    l = ListaDpCirc()

    print("\n1. Inserindo elementos:")
    l.insereNoInicio(3, "Três")
    l.insereNoInicio(2, "Dois")
    l.insereNoInicio(1, "Um")
    l.insereNoFim(4, "Quatro")
    l.insereNoFim(5, "Cinco")

    print("Lista (iterativo):")
    l.mostraLista()

    print("\nLista inversa (iterativo):")
    l.mostraListaInversa()

    # Atividade 2: Recursivo ordem direta
    print("\n2. Mostra recursiva (ordem direta):")
    l.mostraListaRecursivo()

    # Atividade 3: Recursivo ordem inversa (já existia)
    print("\n3. Mostra recursiva (ordem inversa):")
    l.mostraListaInversaRecursivo()

    # Atividade 4: Tamanho iterativo
    print(f"\n4. Tamanho iterativo: {l.tamanhoIterativo()}")

    # Atividade 5: Tamanho recursivo
    print(f"5. Tamanho recursivo: {l.tamanhoRecursivo()}")

    print("\n6. Testando lista vazia:")
    l2 = ListaDpCirc()
    l2.mostraListaRecursivo()
    l2.mostraListaInversaRecursivo()
    print(f"Tamanho iterativo vazio: {l2.tamanhoIterativo()}")
    print(f"Tamanho recursivo vazio: {l2.tamanhoRecursivo()}")

def testar_pilha():
    print("\n" + "=" * 60)
    print("TESTE: Pilha (Stack) - Atividade 6")
    print("=" * 60)

    p = Pilha()

    print("\n1. Empilhando: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        p.push(i, f"Elemento {i}")

    print("Pilha (topo -> base):")
    p.mostraPilha()

    print("\n2. Pilha recursiva:")
    p.mostraPilhaRecursivo()

    print(f"\n3. Topo: {p.top()}")
    print(f"   Tamanho: {p.tamanho()}")

    print("\n4. Desempilhando:")
    while not p.vazia():
        print(f"   Pop: {p.pop()}")

    print(f"\n5. Vazia? {p.vazia()}")

def testar_fila():
    print("\n" + "=" * 60)
    print("TESTE: Fila (Queue) - Atividade 6")
    print("=" * 60)

    f = Fila()

    print("\n1. Enfileirando: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        f.enqueue(i, f"Elemento {i}")

    print("Fila (frente -> fim):")
    f.mostraFila()

    print("\n2. Fila recursiva:")
    f.mostraFilaRecursivo()

    print(f"\n3. Frente: {f.front()}")
    print(f"   Fim: {f.rear()}")
    print(f"   Tamanho: {f.tamanho()}")

    print("\n4. Desenfileirando:")
    while not f.vazia():
        print(f"   Dequeue: {f.dequeue()}")

    print(f"\n5. Vazia? {f.vazia()}")

def testar_deque():
    print("\n" + "=" * 60)
    print("TESTE: Deque - Atividade 7")
    print("=" * 60)

    d = Deque()

    print("\n1. Inserindo no início: 30, 20, 10")
    d.insereInicio(30, "Trinta")
    d.insereInicio(20, "Vinte")
    d.insereInicio(10, "Dez")
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

    print("\n6. Como Pilha (LIFO):")
    d2 = Deque()
    d2.push(1, "Um")
    d2.push(2, "Dois")
    d2.push(3, "Três")
    print(f"   Topo: {d2.top()}")
    print(f"   Pop: {d2.pop()}")
    print(f"   Novo topo: {d2.top()}")

    print("\n7. Como Fila (FIFO):")
    d3 = Deque()
    d3.enqueue(1, "Um")
    d3.enqueue(2, "Dois")
    d3.enqueue(3, "Três")
    print(f"   Frente: {d3.front()}")
    print(f"   Dequeue: {d3.dequeue()}")
    print(f"   Nova frente: {d3.front()}")

    print("\n8. Exibição recursiva direta:")
    d.mostraDequeRecursivo()

    print("\n9. Exibição recursiva inversa:")
    d.mostraDequeInversoRecursivo()

if __name__ == "__main__":
    testar_lista_dupla()
    testar_lista_circ()
    testar_lista_dp_circ()
    testar_pilha()
    testar_fila()
    testar_deque()

    print("\n" + "=" * 60)
    print("TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
    print("=" * 60)