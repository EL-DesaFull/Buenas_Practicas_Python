#PROYECTO ANALIZADOR DE TEXTO

#Pedir al usuario ingresar un texto
texto = input("Ingresar Texto: ")
list_letter = []
letra1 = input("Primera letra de su eleccion: ").lower()
list_letter.append(letra1)

while True:
    letra2 = input("Segunda letra de su eleccion: ").lower()
    if letra2 == letra1:
        print(f"La letra \"{letra2}\" ya fue elegida como opcion")
    else:
        list_letter.append(letra2)
        break

while True:
    letra3 = input("Tercera letra de su eleccion: ").lower()
    if letra3 == letra1 or letra3 == letra2:
        print(f"La letra \"{letra3}\" ya fue elegida como opcion")
    else:
        list_letter.append(letra3)
        break
#PROCESAR
#Minusculas todos
texto = texto.lower()

#Numero de veces que aparece cada una de las letras
cant_apar_l1 = texto.count(list_letter[0])
cant_apar_l2 = texto.count(list_letter[1])
cant_apar_l3 = texto.count(list_letter[2])

if cant_apar_l1 == 1:
    sustantivo = "vez"
else:
    sustantivo = "veces"
print(f"\nLa letra '{letra1}' aparece {cant_apar_l1} {sustantivo}.")

if cant_apar_l2 == 1:
    sustantivo = "vez"
else:
    sustantivo = "veces"
print(f"\nLa letra '{letra2}' aparece {cant_apar_l2} {sustantivo}.")

if cant_apar_l3 == 1:
    sustantivo = "vez"
else:
    sustantivo = "veces"
print(f"\nLa letra '{letra3}' aparece {cant_apar_l3} {sustantivo}.")

#Contar Palabras
separo_texto = texto.split()
print(f"\nA lo largo de todo el texto hay {len(separo_texto)} palabras")

#Primera letra de todo el texto y la ultima letra del texto
first_letter = texto[0]
last_letter = texto[-1]
print(f"\nLa primera letra de todo el texto es '{first_letter}'. "
      f"\nLa ultima letra de todo el texto es '{last_letter}'.")

#Mostrar el texto invertido
separo_texto.reverse()
inv_texto = " ".join(separo_texto)
print(f"\nAsi se veria el texto invertido: '{inv_texto}'.")

#Indicar si la palabra Python existe
siPython = "python" in separo_texto
if siPython:
    resp = "si"
else:
    resp = "no"
print(f"\nLa palabra 'Python' {resp} esta en el texto.")

#Otra forma de buscar que me gusto
buscar_python = "python" in texto
dic = {True:'si', False:'no'}
print(f"\nLa palabra 'Python' {dic[buscar_python]} esta en el texto.")