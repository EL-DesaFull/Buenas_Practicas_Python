import os
from os import system
from pathlib import Path, PureWindowsPath
import time

#1. FUNCIONES *****************************

# funcion que me indica ruta principal y total de recetas
def informacion_relevante():
    # Bienvenida al usuario
    print("Bienvenido")

    # Ruta de acceso al directorio donde se encuentra la carpeta de recetas
    ruta_acceso = Path(Path.home(), "Recetas")

    # Informar cuántas recetas hay en total dentro de esa carpeta
    total_recetas = 0
    msg = ""
    for receta in Path(ruta_acceso).glob("**/*.txt"):
        total_recetas += 1

    if total_recetas == 1:
        msg = f'hay {total_recetas} receta'
    else:
        msg = f'hay {total_recetas} recetas'
    print(f'La ruta de acceso a las recetas es: {ruta_acceso.as_uri()} y {msg}\n')

def mostrar_menu():
    # Listo el Menu Principal
    opcion = lista_menu()
    while opcion != '6':

        #Valido que elija la opcion correcta
        opcion = validar_menu(opcion)

        # Lectura de Recetas.
        if opcion == '1':
            categ_obtenida = obtener_categorias()
            #Valido y obtengo la categoria seleccionada
            val_categ = validar_categoria(categ_obtenida[1], categ_obtenida[0])
            if val_categ[0] and val_categ[3] == 'Salir':
                opcion = lista_menu()
            else:
                #Categoria Seleccionada
                categ_selected = categ_obtenida[0][val_categ[1]]
                #Lista de Recetas
                receta_obtenida = obtener_recetas(categ_selected)
                #Validar Receta Seleccionada
                val_recet = validar_receta_seleccionada(receta_obtenida[1], receta_obtenida[0], categ_selected)
                if val_recet[0] and val_recet[4] != 'Salir':
                    time.sleep(1)
                    system('cls')
                    receta_selected = val_recet[4]
                    leer_receta(categ_selected, receta_selected)
                    retorno = input('Continuar? (y/n): ').lower()
                    while retorno not in ['y','n']:
                        retorno = input('Continuar? (y/n): ').lower()
                    else:
                        if retorno == 'y':
                            time.sleep(1)
                            system('cls')
                            # retorno a las categorias
                            pass
                        else:
                            time.sleep(1)
                            system('cls')
                            opcion = lista_menu()

        #Creacion de Recetas
        elif opcion == '2':
            categ_obtenida = obtener_categorias()
            # Valido y obtengo la categoria seleccionada
            val_categ = validar_categoria(categ_obtenida[1], categ_obtenida[0])
            if val_categ[0] and val_categ[3] == 'Salir':
                opcion = lista_menu()
            else:
                resultado = crear_receta(val_categ[3])
                if resultado == False:
                    opcion = lista_menu()
                else:
                    time.sleep(1)
                    system('cls')
                    # retorno a las categorias
                    pass

        #Creacion de Categoria
        elif opcion == '3':
            resultado = crear_categorias()
            if resultado == False:
                time.sleep(2)
                system('cls')
                opcion = lista_menu()

        #Eliminar Receta
        elif opcion == '4':
            categ_obtenida = obtener_categorias()
            # Valido y obtengo la categoria seleccionada
            val_categ = validar_categoria(categ_obtenida[1], categ_obtenida[0])
            if val_categ[0] and val_categ[3] == 'Salir':
                opcion = lista_menu()
            else:
                # Categoria Seleccionada
                categ_selected = categ_obtenida[0][val_categ[1]]
                # Lista de Recetas
                receta_obtenida = obtener_recetas(categ_selected)
                val_recet = validar_receta_seleccionada(receta_obtenida[1], receta_obtenida[0], categ_selected)
                if val_recet[0] and val_recet[4] != 'Salir':
                    eliminar_recetas(val_recet[4],categ_selected)

        #Eliminar Categoria
        elif opcion == '5':
            categ_obtenida = obtener_categorias()
            val_categ = validar_categoria(categ_obtenida[1], categ_obtenida[0])
            if val_categ[0] and val_categ[3] == 'Salir':
                opcion = lista_menu()
            else:
                # Categoria Seleccionada
                categ_selected = categ_obtenida[0][val_categ[1]]
                eliminar_categoria(categ_selected)
    else:
        system('cls')
        print("Salida, gracias")

def lista_menu():
    time.sleep(1)
    print('Menu Principal\n')
    print(f'1. Lectura de Recetas. \n'
          f'2. Creación de Recetas. \n'
          f'3. Crear Categorias. \n'
          f'4. Eliminar Receta. \n'
          f'5. Eliminar Categoria. \n'
          f'6. Salir del Sistema.\n')
    opcion = input('Seleccione una opción del Menú: ')
    time.sleep(1)
    system('cls')
    return opcion

def validar_menu(opcion):
    if opcion not in ['1', '2', '3', '4', '5']:
        system('cls')
        print(f'El valor ingresado "{opcion}" es errado, intente de nuevo')
        # Listo el Menu Principal
        opcion = lista_menu()
    return opcion

def listar_categoria():
    time.sleep(1)
    dicc_categoria = {}
    nomb_categ = ""
    dir_home = Path(Path.home(), "Recetas")
    cont = 1
    for categoria in dir_home.iterdir():
        dicc_categoria[cont] = categoria.name
        nomb_categ += f'({cont}).{categoria.name}\n'
        cont += 1
    nomb_categ += f'({cont}).Salir\n'
    dicc_categoria[cont] = "Salir"
    print(f'\nCategorias: ')
    print(nomb_categ)
    return dicc_categoria

def obtener_categorias():
    # Hago una lista de las categorias
    dicc_categoria = listar_categoria()
    categ = int(input('Seleccione una Categoria: '))
    return dicc_categoria, categ

def validar_categoria(categ, dicc_categorias):
    time.sleep(1)
    system('cls')
    valor = dicc_categorias.get(categ, False)
    while valor == False:
        system('cls')
        print(f'\nError: La categoria seleccionada es errada.')
        dicc_categorias = listar_categoria()
        categ = int(input('Seleccione una Categoria: '))
        valor = dicc_categorias.get(categ, False)
    else:
        return True, categ, dicc_categorias, valor

def listar_recetas(categoria):
    time.sleep(1)
    if categoria != "Salir":
        dicc_recetas = {}
        nomb_receta = ""
        dir_home = Path(Path.home(), "Recetas", categoria)
        cont = 1
        for receta in dir_home.iterdir():
            dicc_recetas[cont] = receta.name
            nomb_receta += f'({cont}).{receta.name}\n'
            cont += 1
        nomb_receta += f'({cont}).Salir\n'
        dicc_recetas[cont] = "Salir"
        print(f'\nRecetas: ')
        print(nomb_receta)
        return dicc_recetas

def obtener_recetas(categoria):
    time.sleep(1)
    system('cls')
    dicc_recetas = listar_recetas(categoria)
    receta = int(input('Seleccione la receta de su gusto: '))
    return dicc_recetas, receta

def validar_receta_seleccionada(receta, dicc_recetas, categoria):
    valor = dicc_recetas.get(receta, False)
    while valor == False:
        system('cls')
        print(f'\nError: La receta seleccionada es errada.')
        dicc_recetas = listar_recetas(categoria)
        receta = int(input('Seleccione una receta: '))
        valor = dicc_recetas.get(receta, False)
    else:
        return True, receta, dicc_recetas, categoria, valor

def leer_receta(categoria, receta):
    receta_select = Path(Path.home(),'Recetas',categoria, receta)
    print(receta_select.read_text())

def crear_receta(categoria):
    nueva_receta = input('Nueva Receta: ')
    nueva_receta = nueva_receta + '.txt'
    path_receta = Path(Path.home(), 'Recetas', categoria, nueva_receta)
    # validar que no se haya escrito anteriormente
    if not path_receta.exists():

        archivo = open(path_receta, 'w')
        escribo_receta = input(f'Escribe tu receta: \n')
        archivo.write(escribo_receta)
        archivo.close()

        print('La receta se creo correctamente')
        time.sleep(1)
        system('cls')
        return False
    else:
        print('Esta opcion ya existe en el menu')
        return True

def crear_categorias():
    time.sleep(1)
    system('cls')
    nomb_carpeta = input('Indique la nueva categoria: ')
    while nomb_carpeta == "Salir":
        print("El nombre de la categoria es incorrecto")
        nomb_carpeta = input('Indique la nueva categoria: ')
        time.sleep(1)
        system('cls')
    else:
        carpeta = Path(Path.home(), 'Recetas', nomb_carpeta)
        if not carpeta.exists():
            carpeta.mkdir()
            print(f"Categoria creada: {carpeta.stem}.")
            print("La pagina se redireccionara al Menu Principal")
            return False
        else:
            print(f"La categoria {carpeta.stem} ya existe.")
            return True

def eliminar_recetas(receta, categoria):
    time.sleep(1)
    system('cls')
    # Confirmar la eliminacion de la receta
    pedir_confirmacion = input(f"Confirma usted eliminar la receta {receta}? (y/n): ").lower()
    while pedir_confirmacion not in ['y', 'n']:
        print('Respuesta Incorrecta')
        pedir_confirmacion = input(f"Confirma usted eliminar la receta {receta}? (y/n): ").lower()
        time.sleep(1)
        system('cls')
    else:
        if pedir_confirmacion == 'y':
            archivo = Path(Path.home(), 'Recetas', categoria, receta)
            os.remove(archivo)
            print(f"La receta {receta} fue eliminada.")
            time.sleep(2)
            system('cls')
        else:
            time.sleep(1)
            system('cls')

def eliminar_categoria(categoria):
    time.sleep(1)
    system('cls')
    # Confirmar la eliminacion de la categoria
    pedir_confirmacion = input(f"Confirma usted eliminar la categoria {categoria}? (y/n): ").lower()
    while pedir_confirmacion not in ['y', 'n']:
        print('Respuesta Incorrecta')
        pedir_confirmacion = input(f"Confirma usted eliminar la categoria {categoria}? (y/n): ").lower()
        time.sleep(1)
        system('cls')
    else:
        if pedir_confirmacion == 'y':
            directorio = Path(Path.home(), 'Recetas', categoria)

            #Validar contenido del directorio
            content_dir = os.listdir(directorio)
            if not content_dir:
                #El directorio esta vacio
                os.rmdir(directorio)
                print(f"La categoria {categoria} fue eliminada.")
                time.sleep(2)
                system('cls')
            else:
                #El directorio tiene contenido
                print(f"La categoria {categoria} posee elementos, por lo tanto no puede ser eliminada.")
                time.sleep(2)
                system('cls')
        else:
            time.sleep(1)
            system('cls')


# 2. Llamar funciones

informacion_relevante()

mostrar_menu()
