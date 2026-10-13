"""
Árvore Binária de Busca (BST) — DSA / FIAP
Base: "Guia Didático - Implementação de BST em Python"

Regra central: para TODO nó,
    subárvore esquerda < nó < subárvore direita
(vale recursivamente, não só entre pai e filho).
"""


class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None


class BST:
    def __init__(self):
        self.raiz = None  # árvore vazia

    # ---------- INSERÇÃO (iterativa) ----------
    # menor -> esquerda, maior -> direita; para ao achar referência vazia
    def inserir(self, dado):
        novo = No(dado)
        if self.raiz is None:
            self.raiz = novo
            return

        atual = self.raiz
        while True:
            if dado < atual.dado:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            elif dado > atual.dado:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita
            else:
                return  # duplicado: não insere

    # ---------- BUSCA ----------
    # descarta um ramo inteiro a cada comparação -> O(h)
    def buscar(self, dado):
        atual = self.raiz
        while atual is not None:
            if dado == atual.dado:
                return True
            if dado < atual.dado:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return False

    def buscar_contando(self, dado):
        """Retorna quantos nós foram visitados na busca (para comparar BST x AVL)."""
        atual = self.raiz
        visitados = 0
        while atual is not None:
            visitados += 1
            if dado == atual.dado:
                return visitados
            atual = atual.esquerda if dado < atual.dado else atual.direita
        return visitados

    # ---------- EXTREMOS ----------
    # mínimo: vai à esquerda até não haver filho esquerdo (não precisa ser folha!)
    def minimo(self, no=None):
        atual = self.raiz if no is None else no
        if atual is None:
            return None
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.dado

    # máximo: vai à direita até não haver filho direito
    def maximo(self, no=None):
        atual = self.raiz if no is None else no
        if atual is None:
            return None
        while atual.direita is not None:
            atual = atual.direita
        return atual.dado

    # ---------- PERCURSOS ----------
    def em_ordem(self, no):      # esquerda -> nó -> direita (sai ordenado)
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.dado, end=" ")
            self.em_ordem(no.direita)

    def pre_ordem(self, no):     # nó -> esquerda -> direita
        if no is not None:
            print(no.dado, end=" ")
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def pos_ordem(self, no):     # esquerda -> direita -> nó
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.dado, end=" ")

    def em_ordem_lista(self, no, saida=None):
        if saida is None:
            saida = []
        if no is not None:
            self.em_ordem_lista(no.esquerda, saida)
            saida.append(no.dado)
            self.em_ordem_lista(no.direita, saida)
        return saida

    # ---------- ALTURA (recalculada percorrendo; convenção: folha = 1, vazio = 0) ----------
    def altura(self, no):
        if no is None:
            return 0
        return 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    # ---------- REMOÇÃO ----------
    # Caso 1: folha            -> retorna None
    # Caso 2: um filho         -> retorna o único filho (pai "pula" o nó)
    # Caso 3: dois filhos      -> copia o SUCESSOR (mínimo da subárvore direita)
    #                             e remove o sucessor da subárvore direita
    def remover(self, no, dado):
        if no is None:
            return None

        if dado < no.dado:
            no.esquerda = self.remover(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self.remover(no.direita, dado)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda

            sucessor = no.direita
            while sucessor.esquerda is not None:
                sucessor = sucessor.esquerda

            no.dado = sucessor.dado
            no.direita = self.remover(no.direita, sucessor.dado)

        return no

    def excluir(self, dado):
        self.raiz = self.remover(self.raiz, dado)


# ---------------------------------------------------------------------------
# Atividade prática: menu
# ---------------------------------------------------------------------------
def menu():
    arvore = BST()
    while True:
        print("\n1 - Inserir valor")
        print("2 - Buscar valor")
        print("3 - Mostrar em ordem")
        print("4 - Mostrar menor valor")
        print("5 - Mostrar maior valor")
        print("6 - Remover valor")
        print("7 - Encerrar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            arvore.inserir(int(input("Valor: ")))
        elif opcao == "2":
            v = int(input("Valor: "))
            print("Encontrado" if arvore.buscar(v) else "Não encontrado")
        elif opcao == "3":
            arvore.em_ordem(arvore.raiz)
            print()
        elif opcao == "4":
            print("Menor:", arvore.minimo())
        elif opcao == "5":
            print("Maior:", arvore.maximo())
        elif opcao == "6":
            arvore.excluir(int(input("Valor: ")))
        elif opcao == "7":
            break
        else:
            print("Opção inválida")


def testes():
    arvore = BST()
    for v in [61, 43, 77, 16, 55, 69, 85, 11, 31, 49, 59, 65, 73, 81, 89]:
        arvore.inserir(v)

    print("Em ordem:")
    arvore.em_ordem(arvore.raiz)            # 11 16 31 43 49 55 59 61 65 69 73 77 81 85 89
    print("\nBuscar 73:", arvore.buscar(73))  # True
    print("Buscar 100:", arvore.buscar(100))  # False
    print("Mínimo:", arvore.minimo(), "| Máximo:", arvore.maximo())  # 11 | 89

    arvore.excluir(31)  # folha
    arvore.excluir(16)  # agora só tem um filho (11)
    arvore.excluir(77)  # dois filhos -> sucessor 81 sobe
    print("Após remover 31, 16, 77:")
    arvore.em_ordem(arvore.raiz)            # 11 43 49 55 59 61 65 69 73 81 85 89
    print()


# Respostas da atividade:
# (a) Em ordem visita esquerda (menores) -> nó -> direita (maiores), recursivamente,
#     então os valores saem em ordem crescente.
# (b) O mínimo só precisa NÃO ter filho esquerdo; pode ter filho direito
#     (que é maior que ele), então não precisa ser folha.
# (c) Pior formato: árvore degenerada (uma "linha", ex.: inserir 10,20,30,40,50),
#     altura = n, busca vira O(n) como uma lista encadeada.
# (d) O mínimo da subárvore direita é maior que tudo da esquerda e menor que todo
#     o resto da direita — colocá-lo no lugar do nó mantém a propriedade da BST.
#     Além disso ele tem no máximo um filho (direito), então removê-lo é caso 1 ou 2.

if __name__ == "__main__":
    testes()
    # menu()  # descomente para usar o menu interativo
