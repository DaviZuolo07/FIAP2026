def obter_preco_por_kg(codigo_carga):
    if 10 <= codigo_carga <= 20:
        return 100.00
    elif 21 <= codigo_carga <= 30:
        return 250.00
    else:
        return 340.00


def obter_percentual_imposto(codigo_estado):
    if codigo_estado == 1:
        return 35
    elif codigo_estado == 2:
        return 25
    elif codigo_estado == 3:
        return 15
    elif codigo_estado == 4:
        return 5
    else:
        return 0


def calcular_valores_carga(codigo_estado, peso_toneladas, codigo_carga):
    peso_quilos = peso_toneladas * 1000
    preco_por_kg = obter_preco_por_kg(codigo_carga)
    percentual_imposto = obter_percentual_imposto(codigo_estado)

    preco_carga = peso_quilos * preco_por_kg
    valor_imposto = preco_carga * (percentual_imposto / 100)
    valor_total = preco_carga + valor_imposto

    return peso_quilos, preco_carga, valor_imposto, valor_total


def main():
    estado = int(input("Digite o código do estado de origem (1 a 5): "))
    peso = float(input("Digite o peso da carga em toneladas: "))
    codigo = int(input("Digite o código da carga (10 a 40): "))

    peso_kg, preco, imposto, total = calcular_valores_carga(estado, peso, codigo)

    print(f"Peso da carga em quilos: {peso_kg:.2f} kg")
    print(f"Preço da carga: R$ {preco:.2f}")
    print(f"Valor do imposto: R$ {imposto:.2f}")
    print(f"Valor total transportado: R$ {total:.2f}")


main()