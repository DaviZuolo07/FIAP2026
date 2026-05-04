n = int(input("Digite a quantidade de números: "))

while n <= 0:
    n = int(input("Valor inválido. Digite um número maior que 0: "))

vetor = []

for i in range(n):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

soma = 0

for i in range(n):
    soma = soma + vetor[i]

print("Vetor:", vetor)
print("Somatória dos números:", soma)