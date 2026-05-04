lista_nomes = ["Maximus", "Decimus", "Meridius", "Ronaldinho"]

for i in range(len(lista_nomes)):
    for j in range(len(lista_nomes)):
        if i != j:
            if i < j:
                print(f"{lista_nomes[i]} - {lista_nomes[j]}")





