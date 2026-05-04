n = int(input("Digite a quantidade de alunos: "))

while n <= 0:
    n = int(input("Valor inválido. Digite uma quantidade maior que 0: "))

notas = []
soma = 0

for i in range(n):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)
    soma = soma + nota

media = soma / n

iguais = 0
acima = 0
abaixo = 0

for i in range(n):
    if notas[i] == media:
        iguais = iguais + 1
    elif notas[i] > media:
        acima = acima + 1
    else:
        abaixo = abaixo + 1

print("Média da turma:", media)
print("Notas iguais à média:", iguais)
print("Notas acima da média:", acima)
print("Notas abaixo da média:", abaixo)