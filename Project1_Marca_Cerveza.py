# PROYECTO PARA CREAR LA MARCA DE UNA CERVEZA PARTIENDO DE DOS PALABRA CLAVES

# Ingreso los inputs en variables para poder condicionarlos
# Agrego un ciclo para que en caso de no cumplir los requisitos mande un mensaje
while True:
    palabra1 = input("Ingrese una palabra que describa la cerveza: ")
    palabra2 = input("Ingrese otra palabra que describa la cerveza: ")
    # Evaluo que no mande valores vacios
    if len(palabra1) > 0 and len(palabra2) > 0:
        # Evaluo que no sea mas de una palabra
        if len(palabra1.split()) > 1 or len(palabra2.split()) > 1:
            print("Debe ingresar solo una palabra en la descripcion")
        else:
            break;
    else:
        print("Debe agregar la palabra para continuar")
# Creo el nombre de la marca con las primeras cinco letras de la primera palabra y con las tres ultimas de la segunda
print("La cerveza se llama: \n\'" + palabra1[:5] + palabra2[-4:] + "\'")
