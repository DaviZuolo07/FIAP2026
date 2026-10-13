"""
Árvore AVL — DSA / FIAP
Base: slides "Árvores Balanceadas" + "Tutorial de Implementação — Evoluindo uma BST para AVL"

O que a AVL acrescenta à BST:
  1. cada nó guarda sua ALTURA (folha = 1, subárvore vazia = 0)
  2. FATOR DE BALANCEAMENTO: FB(n) = altura(esquerda) - altura(direita)
     AVL válida: FB de todo nó em {-1, 0, +1}
  3. ROTAÇÕES quando FB vira +2 ou -2 (só reorganizam referências, não mudam dados
     nem a ordem — busca, mínimo, máximo e em ordem continuam iguais à BST)
"""

from BST import BST


class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1  # única novidade em relação ao nó da BST


class AVL:
    def __init__(self):
        self.raiz = None
        self.ultimo_caso = None  # só para os testes mostrarem qual rotação ocorreu

    # ---------- ALTURA E FB ----------
    def altura(self, no):
        # consulta o valor guardado, NÃO percorre a árvore -> O(1)
        if no is None:
            return 0
        return no.altura

    def atualizar_altura(self, no):
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    # ---------- ROTAÇÕES ----------
    #  Rotação à direita (corrige peso à ESQUERDA)
    #        y              x
    #       /                \
    #      x        ->        y
    #       \                /
    #        T2            T2
    def rotacao_direita(self, y):
        x = y.esquerda
        temp = x.direita       # T2 precisa ser preservada

        x.direita = y
        y.esquerda = temp

        self.atualizar_altura(y)  # primeiro quem desceu
        self.atualizar_altura(x)  # depois a nova raiz
        return x                  # nova raiz da subárvore

    #  Rotação à esquerda (corrige peso à DIREITA) — simétrica
    #      x                  y
    #       \                /
    #        y      ->      x
    #       /                \
    #     T2                  T2
    def rotacao_esquerda(self, x):
        y = x.direita
        temp = y.esquerda

        y.esquerda = x
        x.direita = temp

        self.atualizar_altura(x)
        self.atualizar_altura(y)
        return y

    # ---------- INSERÇÃO (recursiva, para rebalancear na volta) ----------
    # Fluxo dos slides:
    #   1. insere como BST  2. atualiza altura na volta da recursão
    #   3. calcula FB       4. se fora de [-1,1], identifica o caso
    #   5. rotaciona        6. devolve a nova raiz da subárvore
    def inserir_recursivo(self, no, dado):
        if no is None:
            return No(dado)

        if dado < no.dado:
            no.esquerda = self.inserir_recursivo(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self.inserir_recursivo(no.direita, dado)
        else:
            return no  # duplicata não é inserida

        self.atualizar_altura(no)
        fb = self.fator_balanceamento(no)

        # LL: pesada à esquerda, em linha reta -> rotação simples à direita
        if fb > 1 and dado < no.esquerda.dado:
            self.ultimo_caso = "LL"
            return self.rotacao_direita(no)

        # RR: pesada à direita, em linha reta -> rotação simples à esquerda
        if fb < -1 and dado > no.direita.dado:
            self.ultimo_caso = "RR"
            return self.rotacao_esquerda(no)

        # LR: pesada à esquerda, zig-zag -> esquerda no filho, depois direita no nó
        if fb > 1 and dado > no.esquerda.dado:
            self.ultimo_caso = "LR"
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        # RL: pesada à direita, zig-zag -> direita no filho, depois esquerda no nó
        if fb < -1 and dado < no.direita.dado:
            self.ultimo_caso = "RL"
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def inserir(self, dado):
        # atribuir a self.raiz é essencial: uma rotação pode trocar a raiz
        self.raiz = self.inserir_recursivo(self.raiz, dado)

    # ---------- REUTILIZADOS DA BST (mesma lógica) ----------
    def buscar(self, dado):
        atual = self.raiz
        while atual is not None:
            if dado == atual.dado:
                return True
            atual = atual.esquerda if dado < atual.dado else atual.direita
        return False

    def buscar_contando(self, dado):
        atual = self.raiz
        visitados = 0
        while atual is not None:
            visitados += 1
            if dado == atual.dado:
                return visitados
            atual = atual.esquerda if dado < atual.dado else atual.direita
        return visitados

    def minimo(self):
        atual = self.raiz
        if atual is None:
            return None
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.dado

    def maximo(self):
        atual = self.raiz
        if atual is None:
            return None
        while atual.direita is not None:
            atual = atual.direita
        return atual.dado

    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.dado, end=" ")
            self.em_ordem(no.direita)

    def em_ordem_lista(self, no, saida=None):
        if saida is None:
            saida = []
        if no is not None:
            self.em_ordem_lista(no.esquerda, saida)
            saida.append(no.dado)
            self.em_ordem_lista(no.direita, saida)
        return saida

    # ---------- VISUALIZAÇÃO ----------
    # direita em cima, nó no meio, esquerda embaixo (vire a cabeça para a esquerda)
    def mostrar(self, no, nivel=0):
        if no is None:
            return
        self.mostrar(no.direita, nivel + 1)
        print("    " * nivel + str(no.dado)
              + f" (h={no.altura}, FB={self.fator_balanceamento(no)})")
        self.mostrar(no.esquerda, nivel + 1)

    # ---------- VALIDAÇÃO ----------
    def verificar_balanceamento(self, no):
        if no is None:
            return True
        if abs(self.fator_balanceamento(no)) > 1:
            return False
        return (self.verificar_balanceamento(no.esquerda)
                and self.verificar_balanceamento(no.direita))

    # ---------- EXTRA: remoção com rebalanceamento ----------
    # (o tutorial deixa para atividade posterior; remover também pode desbalancear)
    # Na remoção não dá para usar "dado" para escolher o caso: usa-se o FB do filho.
    def remover_recursivo(self, no, dado):
        if no is None:
            return None

        if dado < no.dado:
            no.esquerda = self.remover_recursivo(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self.remover_recursivo(no.direita, dado)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            sucessor = no.direita
            while sucessor.esquerda is not None:
                sucessor = sucessor.esquerda
            no.dado = sucessor.dado
            no.direita = self.remover_recursivo(no.direita, sucessor.dado)

        self.atualizar_altura(no)
        fb = self.fator_balanceamento(no)

        if fb > 1 and self.fator_balanceamento(no.esquerda) >= 0:   # LL
            return self.rotacao_direita(no)
        if fb > 1 and self.fator_balanceamento(no.esquerda) < 0:    # LR
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        if fb < -1 and self.fator_balanceamento(no.direita) <= 0:   # RR
            return self.rotacao_esquerda(no)
        if fb < -1 and self.fator_balanceamento(no.direita) > 0:    # RL
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def excluir(self, dado):
        self.raiz = self.remover_recursivo(self.raiz, dado)


# ---------------------------------------------------------------------------
# TESTES (slides 15/16 e tutorial etapas 11–13)
# ---------------------------------------------------------------------------
def testes_calibracao():
    print("=== Testes de calibração (os 4 casos) ===")
    casos = [([30, 20, 10], "LL"), ([10, 20, 30], "RR"),
             ([30, 10, 20], "LR"), ([10, 30, 20], "RL")]
    for seq, esperado in casos:
        arvore = AVL()  # árvore nova para cada teste
        for v in seq:
            arvore.inserir(v)
        print(f"\nSequência {seq} -> caso {arvore.ultimo_caso} (esperado {esperado}),"
              f" raiz = {arvore.raiz.dado}")
        arvore.mostrar(arvore.raiz)
        print("Em ordem:", *arvore.em_ordem_lista(arvore.raiz))


def teste_estresse():
    print("\n=== Teste de estresse: 10, 20, 30, 40, 50, 25 ===")
    arvore = AVL()
    for v in [10, 20, 30, 40, 50, 25]:
        arvore.inserir(v)
    arvore.mostrar(arvore.raiz)
    # esperado: raiz 30, altura 3
    #         30
    #        /  \
    #      20    40
    #     /  \     \
    #   10   25     50
    print("Raiz:", arvore.raiz.dado, "| Altura:", arvore.altura(arvore.raiz))
    print("Em ordem:", *arvore.em_ordem_lista(arvore.raiz))
    print("Balanceada?", arvore.verificar_balanceamento(arvore.raiz))


def comparar_bst_avl():
    print("\n=== BST x AVL inserindo 1..100 em ordem crescente ===")
    bst, avl = BST(), AVL()
    for v in range(1, 101):
        bst.inserir(v)
        avl.inserir(v)
    print("Altura BST:", bst.altura(bst.raiz))   # 100 (degenerada, vira lista)
    print("Altura AVL:", avl.altura(avl.raiz))   # 7
    print("Nós visitados buscando 100 -> BST:", bst.buscar_contando(100),
          "| AVL:", avl.buscar_contando(100))


def teste_remocao():
    print("\n=== Extra: remoção na AVL ===")
    arvore = AVL()
    for v in [10, 20, 30, 40, 50, 25]:
        arvore.inserir(v)
    arvore.excluir(10)
    arvore.excluir(25)  # 30 fica com FB = -1: ainda válido, sem rotação
    arvore.excluir(20)  # 30 fica com FB = -2 e FB(40) = -1 -> caso RR
    arvore.mostrar(arvore.raiz)
    print("Balanceada?", arvore.verificar_balanceamento(arvore.raiz))


if __name__ == "__main__":
    testes_calibracao()
    teste_estresse()
    comparar_bst_avl()
    teste_remocao()
