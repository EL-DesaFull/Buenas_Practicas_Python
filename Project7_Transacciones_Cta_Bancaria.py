from os import system
from random import randint

#Clases

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nNúmero de Cuenta: {self.numero_cuenta}\nBalance: {self.balance}"

    def depositar(self, deposito):
        print(f"Saldo Anterior: {self.balance}\nMonto a depositar: {deposito}")
        self.balance += deposito
        print(f"Saldo Actual: {self.balance}")
        return self.balance

    def retirar(self, retiro):
        if retiro > self.balance:
            print(f"No se admite el retiro, no tiene suficiente saldo en su cuenta.")
            print(f"Saldo Actual: {self.balance}")
            return self.balance
        elif retiro <= self.balance:
            print(f"Saldo Anterior: {self.balance}\nMonto a retirar: {retiro}")
            self.balance -= retiro
            print(f"Saldo Actual: {self.balance}")
            return self.balance

#Funciones

def crear_cliente():
    nombre = input('Nombre del Cliente: ')
    apellido = input('Apellido del Cliente: ')
    numero_cuenta = randint(1000, 9999)
    saldo = 0
    mi_cliente = Cliente(nombre, apellido, numero_cuenta, saldo)
    return mi_cliente

def lista_opciones():
    print('\nMenu de Transacciones')
    print('1.Depositos \n2.Retiros \n3.Salir')
    opcion = input('Seleccione una opción: ')
    system('cls')
    return opcion

def mostrar_opciones(cliente):
    # Lista de opciones
    opcion = lista_opciones()
    while opcion != '3':
        #Valido que elija la opcion correcta
        opcion = validar_opcion(opcion)
        if opcion == '1':
            # llamo la funcion depositar de la instancia de la clase Cliente
            monto_deposito = input('Indique el monto a depositar: ')
            cliente.depositar(float(monto_deposito))
            continuar = continuar_transaccion()
            if continuar == 's':
                opcion = lista_opciones()
            else:
                opcion = '3'
        elif opcion == '2':
            # llamo la funcion retirar de la instancia de la clase Cliente
            monto_retirar = input('Indique el monto a retirar: ')
            cliente.retirar(float(monto_retirar))
            continuar = continuar_transaccion()
            if continuar == 's':
                opcion = lista_opciones()
            else:
                opcion = '3'
    else:
        print("Ha salido del sistema.")

def validar_opcion(opcion):
    if opcion not in ['1','2','3']:
        system('cls')
        print(f'La opcion ingresada "{opcion}" no es correcta, intente de nuevo.')
        opcion = lista_opciones()
    return opcion

def continuar_transaccion():
    final = input('Desea continuar con otra transaccion? (S)Si / (N)No ').lower()
    while final not in ['s','n']:
        print('Respuesta invalida')
        final = input('Desea continuar con otra transaccion? (S)Si / (N)No ').lower()
    else:
        return final

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    mostrar_opciones(mi_cliente)

#Ejecucion
inicio()

