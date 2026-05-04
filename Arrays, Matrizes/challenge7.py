nomes = []

while True:
    nome = input("Digite um nome ou aperte Enter para parar: ")

    if nome.strip() == "":
        break

    nomes.append(nome)

print("Nomes na ordem inversa:")

for i in range(len(nomes) - 1, -1, -1):
    print(nomes[i])