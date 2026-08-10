eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
    }
print(eng2sp)
print(eng2sp["two"])
print(len(eng2sp))

# Operador IN
# Acusa se algo aparecer como chave dicionário
print('one' in eng2sp)

# Values()
valores_dict = eng2sp.values()
print('uno' in valores_dict)

# Contador de LETRAS
def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

count = count_letters("Gordinho sensual")
print(count)