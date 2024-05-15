#proyecto para conocer comisiones ganadas

while True:
    #Datos de entreda
    nmbr_empld = input("Indique su nombre y apellido: ")
    # Evaluo que no mande valores vacios
    if len(nmbr_empld) > 0:
        #paso el siguiente valor
        mnt_ttl_vnts = input("Indique el monto total en ventas: ")
        #hago un try por si pasa cadena de texto y no un numero
        try:
            #conversion al tipo float
            mnt_ttl_vnts = float(mnt_ttl_vnts)
            # operacion de comision
            mnt_cmsion = (mnt_ttl_vnts * 13)/100
            break
        except ValueError:
            print("El valor introducido no es un número.")
    else:
        print("No ha ingresado datos del vendedor")
print(f"El Sr(a) {nmbr_empld}, en este mes obtuvo un monto en comisiones de: {round(mnt_cmsion,2)}$")