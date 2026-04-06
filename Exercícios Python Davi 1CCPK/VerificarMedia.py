def verificar_situacao(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >=7:
        return f"Média: {media:.2f} - Aprovado!"
    elif media >= 5:
        return f"Média: {media:.2f} - Em Recuperação!"
    else:
        return f"Média: {media:.2f} - Reprovado!"

def main():
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite sua segunda nota: "))
    n3 = float(input("Digite sua terceira nota: "))
    n4 = float(input("Digite sua quarta nota: "))

    resultado = verificar_situacao(n1, n2, n3, n4)
    print(resultado)


main()