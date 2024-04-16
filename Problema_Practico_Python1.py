'''Funcion para practicar utilizando *args,
que recibe numeros enteros:
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver
el número de valor intermedio.'''
def devolver_distintos(*enteros):
    num = list(enteros)
    suma_ent = sum(num)
    if suma_ent >= 10 and suma_ent <= 15:
        num.sort()
        return (num[1])
    elif suma_ent > 15:
        return (max(enteros))
    elif suma_ent < 10:
        return (min(enteros))
print(devolver_distintos(5,6,7))

#----SOLUCION PROPUESTA POR EL PROFESOR

def devolver_distintos2(a,b,c):
    suma = a + b + c
    lista = [a, b, c]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]
print(devolver_distintos2(20,5,7))
print(devolver_distintos2(3,2,4))
print(devolver_distintos2(7,2,3))
