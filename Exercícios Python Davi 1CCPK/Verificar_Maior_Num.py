def verificar_maior(num1, num2):
    if num1 > num2:
        return f"O maior número é: {num1}."
    elif num2 > num1:
        return f"O maior número é: {num2}."
    else:
        return "Os dois números são iguais."

def main():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    resultado = verificar_maior(n1, n2)
    print(resultado)

main()