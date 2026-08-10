# Recebe os e-mails
entrada = input("Digite os e-mails separados por vírgula: ")

# Separa os e-mails
emails = entrada.split(",")

# Lista para armazenar os usuários
usuarios = []

# Dicionário para contar os domínios
dominios = {}

# Analisa cada e-mail
for email in emails:
    email = email.strip()

    # Separa usuário e domínio
    usuario, dominio = email.split("@")

    # Adiciona o usuário na lista
    usuarios.append(usuario)

    # Conta o domínio
    if dominio in dominios:
        dominios[dominio] += 1
    else:
        dominios[dominio] = 1

# Converte a lista de usuários para tupla
usuarios = tuple(usuarios)

# Exibe primeiro e último usuário
print("\nPrimeiro usuário:", usuarios[0])
print("Último usuário:", usuarios[-1])

# Troca primeiro e último usando atribuição de tupla
usuarios_lista = list(usuarios)
usuarios_lista[0], usuarios_lista[-1] = usuarios_lista[-1], usuarios_lista[0]
usuarios = tuple(usuarios_lista)

# Relatório
print("\nRelatório:")
print("Quantidade de e-mails por domínio:")

for dominio, quantidade in dominios.items():
    print(f"{dominio}: {quantidade}")

print("Lista de usuários:", tuple(usuarios_lista))

# Para mostrar o resultado após a troca
print("Após troca de posições:", usuarios)