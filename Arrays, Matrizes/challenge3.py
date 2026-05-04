import random
vetor = []
n = int(input("Digite um número: "))

for i in range(n):
    vetor.append(random.randint(0, 9))

print(vetor)