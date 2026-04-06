def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# TESTE

n = int(input("Digite um número: "))
resultado = verificar_par_ou_impar(n)
print(f"O número {n} é: {resultado}.")
