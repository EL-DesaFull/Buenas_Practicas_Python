from random import *

#Iniciamos preguntando por el nombre del jugador
player = input("Bienvenido jugador, ¿Cómo te llamas? ")
while len(player) > 0:
    play_guess_numb = input(f"{player}, quieres participar de un juego (s/n): ")
    while play_guess_numb == 's':
        print(f"{player}, Debes adivinar el numero que he seleccionado en un rango del 1 al 100.\nSolo tienes ocho(8) intentos. Que comience el juego!")
        num_ram = randint(1, 101)
        for num in range(1,9):
            player_intent = input(f"Intento {num}: ")

            if not player_intent.isdigit():
                print("¡Error! Debe ingresar un número entero.")
                continue
            player_intent = int(player_intent)

            if player_intent == num_ram:
                print(f"Felicitaciones! has acertado en {num} intentos!")
                break
            elif player_intent not in range(1,101):
                print("Ha elegido un numero fuera del rango del 1 al 100")
            elif player_intent < num_ram:
                print("Respuesta incorrecta. Su numero es menor al numero secreto")
            elif player_intent > num_ram:
                print("Respuesta incorrecta. Su numero es mayor al numero secreto")

            if num == 8:
                print(f"{player}, has perdido. El numero secreto era: {num_ram}")

        play_guess_numb = input("Quieres jugar otra vez (s/n):")
    else:
        if play_guess_numb == 'n':
            print(f"Selecciono la opcion '{play_guess_numb}', el juego se cierra. Adios!")
            break
        else:
            print(f"Respuesta errada: '{play_guess_numb}'!")
else:
    print("No proporciono datos de jugador.")