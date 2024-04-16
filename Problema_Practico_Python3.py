'''función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas'''

def cero_repetido(*args):
    #num = 0
    repetido = False
    for indice,arg in enumerate(args):
        if indice == 0:
            num = args[indice]
            #print(args[indice])
        if indice > 0:
            if num == args[indice]:
                print(f'el num: {num} es igual a el args: {args[indice]} en el indice: {indice}')
                return True
            else:
                repetido = False
            num = args[indice]
    return repetido
print(cero_repetido(0,10,20,30,40,50,0))

#----SOLUCION PROPUESTA POR EL PROFESOR
def ceros_vecinos(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False
print(ceros_vecinos(0,6,0,51,51,1,51,84,1,55,54,84,8,0,0))



