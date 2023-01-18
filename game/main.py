import random

user_wins = 0
computer_wins = 0
empate = 0

while True:
    # pedirle al usuario que elija piedra, papel o tijera
    user_choice = int(input("""Selecciona una opción: 
                        1: Piedra
                        2: Papel
                        3: Tijera
                        Yo elijo: """))

    # generar una elección aleatoria para la computadora
    computer_choice = random.choice([1,2,3])

    # comparar las elecciones para determinar el ganador
    if user_choice == computer_choice:
        print("Empate!")
        empate +=1
    elif user_choice == 1 and computer_choice == 3:
        print("Ganaste!")
        user_wins += 1
    elif user_choice == 2 and computer_choice == 1:
        print("Ganaste!")
        user_wins += 1
    elif user_choice == 3 and computer_choice == 2:
        print("Ganaste!")
        user_wins += 1
    else:
        print("Perdiste.")
        computer_wins += 1

    # imprimir el número de juegos ganados por el usuario y la computadora
    print("Juegos ganados por el usuario:", user_wins)
    print("Juegos ganados por la computadora:", computer_wins)
    print("juegos empatados: ", empate)
