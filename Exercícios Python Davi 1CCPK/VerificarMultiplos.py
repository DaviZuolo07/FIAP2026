def verificar_multiplos(A, B):
    if A % B == 0 or B % A == 0:
        return "São Múltiplos"
    else:
        return "Não são múltiplos"


def main():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))

    resultado = verificar_multiplos(A, B)
    print(resultado)

main()