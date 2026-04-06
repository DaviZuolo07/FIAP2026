def classificar_triangulo(lado1, lado2, lado3):
    lados = sorted([lado1, lado2, lado3], reverse=True)
    A, B, C = lados

    resultados = []

    if A >= B + C:
        resultados.append("NAO FORMA TRIANGULO")
    else:
        if A**2 == B**2 + C**2:
            resultados.append("TRIANGULO RETANGULO")
        elif A**2 > B**2 + C**2:
            resultados.append("TRIANGULO OBTUSANGULO")
        else:
            resultados.append("TRIANGULO ACUTANGULO")

        if A == B == C:
            resultados.append("TRIANGULO EQUILATERO")
        elif A == B or A == C or B == C:
            resultados.append("TRIANGULO ISOSCELES")

    return resultados


def main():
    x = float(input("Digite o primeiro lado: "))
    y = float(input("Digite o segundo lado: "))
    z = float(input("Digite o terceiro lado: "))

    resultado = classificar_triangulo(x, y, z)

    for mensagem in resultado:
        print(mensagem)


main()