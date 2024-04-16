'''Función que recibe cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.'''
def alphabe_letter_word(word):
    letters1 = list(word.lower())
    letters1.sort()
    letters2 = []
    letra = ""
    for letter in letters1:
        busqueda = letter in letters2
        if busqueda == False:
            letters2.append(letter)
    return letters2

devuelto = alphabe_letter_word("entretenido")
print(devuelto)

#----SOLUCION PROPUESTA POR EL PROFESOR
def letras_unicas(palabra):
    #usar set porque usa valores unicos y si estan repetidos los ignora
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista

print(letras_unicas('entretenido'))
print(letras_unicas('cascarabias'))