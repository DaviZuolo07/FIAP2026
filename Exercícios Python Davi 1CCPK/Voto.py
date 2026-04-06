from datetime import datetime

def verificar_tipo_voto(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return f"Idade aproximada: {idade} anos - Voto proibido este ano."
    elif idade < 18 or idade > 70:
        return f"Idade aproximada: {idade} anos - Voto opcional este ano."
    else:
        return f"Idade aproximada: {idade} anos - Voto obrigatório este ano."


def main():
    ano = int(input("Digite o ano de nascimento: "))
    resultado = verificar_tipo_voto(ano)
    print(resultado)


main()