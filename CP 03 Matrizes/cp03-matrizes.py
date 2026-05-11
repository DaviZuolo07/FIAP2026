temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_quantidade_criticos = 0
sala_maior_criticos = 0

for i in range(len(temperaturas)):
    soma = 0
    registros_criticos = 0

    for j in range (len(temperaturas[i])):
        soma += temperaturas[i][j]

        if temperaturas[i][j] >= 33:
            registros_criticos += 1
    media = soma / len(temperaturas[i])

    print(f"Sala {i + 1}")
    print(f"Média das temperaturas: {media:.2f}")
    print(f" Quantidade de registros críticos: {registros_criticos}")
    print()

    if registros_criticos > maior_quantidade_criticos:
        maior_quantidade_criticos = registros_criticos
        sala_maior_criticos = i + 1

print(f"A sala com maior quantidade de registros críticos foi a Sala: {sala_maior_criticos}.")
