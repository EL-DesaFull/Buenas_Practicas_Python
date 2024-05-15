from random import choice

#1.Variables Globales ************************************

#Lista de palabras
palabras = ["Amigo", "Altar", "Altura", "Amanecer", "Belleza", "Biblioteca", "Bosque", "Brisa", "Bondad", "Carisma", "Cascada", "Celeste", "Ceniza", "Deseo", "Destino", "Diamante", "Dificultad", "Discurso", "Enigma", "Equilibrio", "Escenario", "Felicidad", "Flor", "Fuego", "Galaxia", "Gato", "Generosidad", "Gigante", "Honestidad", "Horizonte", "Historia", "Idea", "Imagen", "Juego", "Juventud", "Justicia", "Juez", "Karma", "King", "Konnichiwa", "Koala", "Libertad", "Libro", "Luz", "Luna", "Magia", "Mar", "Mariposa", "Naturaleza", "Noche", "Nombre", "Nube", "Noticia", "Ojo", "Ola", "Oportunidad", "Oscuridad", "Palabras", "Paz", "Peligro", "Pensamiento", "Perro", "Quijote", "Quietud", "Queso", "Quimera", "Risa", "Romance", "Rosa", "Regalo", "Sacrificio", "Sonrisa", "Sol", "Tiempo", "Tierra", "Tesoro", "Tormenta", "Trabajo", "Universo", "Urgencia", "Vacaciones", "Velocidad", "Victoria", "Verdad", "Whisky", "Wifi", "Yogur", "Yate", "Yeti", "Yoyo", "Yunque", "Zorro", "Zumo", "Zafiro"]

#2. Funciones ********************************************

# Funcion para seleccionar nivel del juego
def nivel_juego(nivel):
    nivel = nivel.lower()
    lista = ['a', 'b', 'c', 'd']
    while nivel not in lista:
        nivel = input(f'Seleccion incorrecta. Seleccione la opcion correcta: ')
    else:
        if nivel == 'a': #Muy Facil
            intento = 6
        elif nivel == 'b': #Facil
            intento = 5
        elif nivel == 'c': #Medio
            intento = 4
        elif nivel == 'd': #dificil
            intento = 3
    return intento

#Funcion que retorna una palabra al azar de una lista
def random_word(words):
    palabra_azar = choice(words)
    palabra_azar = palabra_azar.lower()
    print(f'La cantidad de letras es: {len(palabra_azar)}')
    return palabra_azar

#funcion que retorna una palabra ofuscada
def palabra_ofuscada(word_random):
    # Casteo la palabra random en una lista
    letras = list(word_random)
    # reemplazo las letras por guiones
    guiones = ['_' for n in letras]
    # lo retorno en una sola palabra
    return "".join(guiones)

#funcion para adivinar una palabra aleatoria letra por letra en un rango de intentos definidos por el nivel elegido
def adivina_palabra(intento, ram_word, word_ofusc):
    cadena = [] #variable para listar el resultado de los intentos
    logrado = False #defino si lo logro o no
    str_cadena1 = "" #resultado final de los ingresado por el usuario
    while intento > 0:
        tu_letra = input('Ingresa tu letra: ')
        tu_letra = tu_letra.lower()
        if validar_entrada(tu_letra):
            busca_tu_letra = ram_word.find(tu_letra)
            if busca_tu_letra != -1:
                str_cadena1 = validar_busqueda(ram_word, cadena, tu_letra, str_cadena1)
                print(str_cadena1)
                if str_cadena1 == ram_word:
                    logrado = True
                    break
            else:
                if len(str_cadena1) == 0:
                    print(word_ofusc)
                else:
                    print(str_cadena1)
                intento -= 1
                intentos_validos(intento)
                logrado = False
        else:
            intento -= 1
            intentos_validos(intento)
    return logrado

#funcion para validar que el usuario ingrese una letra valida
def validar_entrada(letra):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if letra not in alphabet:
        print(f"Ingresaste un valor invalido '{letra}'. Pierdes un turno.")
        return False
    else:
        return True

#funcion que valida la busqueda de la letra ingresada y genera la cadena con guiones de letras restantes
def validar_busqueda(ram_word, cadena, tu_letra, str_cadena):
    for indice, letra in enumerate(ram_word):
        if tu_letra != letra:
            if len(ram_word) != len(str_cadena):
                cadena.append('_')
        else:
            if len(ram_word) == len(str_cadena):
                cadena[indice] = tu_letra
            else:
                cadena.append(tu_letra)
        str_cadena1 = "".join(cadena)
    return str_cadena1

#funcion mensajes devueltos
def mensaje_resultado(resultado, ram_word):
    msg = ""
    if resultado:
        msg = f'Lo lograstes, buen trabajo!!!'
    else:
        msg = f"No lo lograste, la palabra era '{ram_word}'"
    return msg

#funcion que indica cuantos intentos quedan
def intentos_validos(intento):
    if intento > 1:
        print(f"Te quedan {intento} intentos")
    elif intento == 1:
        print(f"Te queda {intento} intento")
    else:
        print(f"Ya no te quedan intentos")

# ***********************************************************************************************************

#3. Ingreso de datos por el usuario
print("***********************************************************")
print("********************* EL AHORCADO *************************")
print("***********************************************************")
print("NIVELES:\n (a)Muy Facil *** 6 intentos.\n (b)Facil ******* 5 intentos.\n (c)Medio ******* 4 intentos.\n (d)Dificil ***** 3 intentos.\n ")

select_level = input('Selecciona tu nivel: ')

#4. Invocacion de las funciones

#Selecciono el nivel del Juego
intento = nivel_juego(select_level)
print(f'El numero de intentos es: {intento}')

#Asigno a una variable la random word
ram_word = random_word(palabras)

# Muestro la palabra con guiones
word_ofusc = palabra_ofuscada(ram_word)

# Comenzar preguntando al usuario por las letras a ingresar
resultado = adivina_palabra(intento, ram_word, word_ofusc)

# Imprimir respuesta final
print(mensaje_resultado(resultado, ram_word))

#*******************************************************
