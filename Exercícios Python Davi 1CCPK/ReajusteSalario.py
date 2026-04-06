def calcular_reajuste(salario):
    if salario <= 280:
        percentual = 20
    elif salario <= 700:
        percentual = 15
    elif salario <= 1500:
        percentual = 10
    else:
        percentual = 5
    valor_aumento = salario * (percentual / 100)
    novo_salario = salario + valor_aumento

    return salario, percentual, valor_aumento, novo_salario

def main():
    salario = float(input("Digite o salário do colaborador: R$ "))
    salario_antigo, percentual, aumento, salario_novo = calcular_reajuste(salario)

    print(f"Salário antes do reajuste: R$ {salario_antigo:.2f}")
    print(f"Percentual de aumento aplicado: {percentual}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário após o reajuste: R$ {salario_novo:.2f}")

main()