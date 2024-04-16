from primefac import isprime

def contar_primos(n):
    num_primo = []
    for nprimo in range(0,n + 1):
        if nprimo != 0 and nprimo != 1:
            if isprime(nprimo):
                num_primo.append(nprimo)
    print(f'Lista de numeros primos: {num_primo}')
    return len(num_primo)

print(f'El total de numeros primos es: {contar_primos(50)}')

#----SOLUCION PROPUESTA POR EL PROFESOR

def contar_primos2(numero):

    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos2(50))

