def pregunta1(lista1, lista2):
    return set(lista1) - set(lista2)

lista1 = [1,2,3,4,5]
lista2 = [3,4,5]

print(pregunta1(lista1,lista2))