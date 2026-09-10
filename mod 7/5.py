lista = [2,5,6,8]
def f(lista):
    lista1 = []
    for luku in lista:
        if luku % 2 ==0:
            lista1.append(luku)
    return lista1
print(lista)
print(f(lista))