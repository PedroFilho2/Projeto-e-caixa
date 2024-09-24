import random

Jogada = int(input("ESCOLHA UMA OPÇÃO:[ 0- PEDRA | 1- PAPEL| 2- TESOURA]:"))
cpu = random.randint(0,2)


#Player ganha?
if Jogada == 0 and cpu == 2: 
    print("Player Venceu!")
if Jogada == 1 and cpu == 0: 
    print("Player Venceu!")
if Jogada == 2 and cpu == 1: 
    print("Player Venceu!")

# CPU GANHAR
if Jogada == 0 and cpu == 1:
    print("CPU Venceu!")
if Jogada == 1 and cpu == 2:
    print("CPU Venceu!")
if Jogada ==2 and cpu == 0:
    print("CPU Venceu!")

#Empate 
if Jogada == 0 and cpu == 0:
    print("Empate!")
if Jogada == 1 and cpu == 1:
    print("Empate!")
if Jogada ==2 and cpu == 2:
    print("Empate!")
