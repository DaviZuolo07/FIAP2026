def calcular(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            return "Erro: divisão por zero não é permitida."
        return numero1 / numero2
    else:
        return "Erro: operação inválida."


def main():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    op = input("Digite a operação (+, -, *, /): ")

    resultado = calcular(n1, n2, op)
    print(f"Resultado: {resultado}")


main()