t = ('a', 'b', 'c', 'd', 'e')
print(t[0])

# Tupla de um único elemento
t1 = 'a',
print(type(t1))

t = tuple() # tupla vazia

t = tuple("texto")
print(t[0])
print(t[1:3])

# com tuples sao imutaveis, vc nao pode alterar os elementos
# masss ... vc pode substituir uma tupla por outra

t = ("T",) + t[1:]
print(t)

# ATRIBUIÇÃO DE TUPLAS
# trocar a com n
a = 5
b = 10

print(f"a: {a}, b: {b}")

temp = a #5
a = b # a = 10
b = temp # b = 5
print(f"a: {a}, b: {b}")

a, b = b, a

print(f"a: {a}, b: {b}")


# SEPARAÇÃO DE E-MAIL

email = "davi.zuolo07@gmail.com"
username, domain = email.split("@")
