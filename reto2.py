import math

def juego(jugador1, jugador2):
    lista = ["papel", "tijera", "piedra"]
    index1 = lista.index(jugador1)
    index2 = lista.index(jugador2)
    dif = index2 - index1
    print(index1)
    print(index2)
    print(dif)
    if index1 == 0:
        if dif == 0:
            ganador = "ninguno"
        if dif == 1:
            ganador = "jugador2"
        if dif == 2:
            ganador = "jugador1"
    else:
        if index1 == 1:
            if dif == 0:
                ganador = "ninguno"
            if dif == 1:
                ganador = "jugador2"
            if dif == -1:
                ganador = "jugador1"
        else:
            if index1 == 2:
                if dif == 0:
                    ganador = "ninguno"
                if dif == -1:
                    ganador = "jugador1"
                if dif == -2:
                    ganador = "jugador2"
            else:
                ganador="no entre"
    return ganador


def main():
    contador = 0
    partidas1 = 0
    partidas2 = 0

    while contador < 3:
        jugador1 = (input('Ingrese "piedra, "papel" o "tijera" para el jugador 1: '))
        jugador2 = (input('Ingrese "piedra, "papel" o "tijera" para el jugador 2: '))
        ganador = juego(jugador1, jugador2)
        print (f'El ganador es: {ganador}')
        if ganador == "jugador1":
            partidas1+=1
        if ganador == "jugador2":
            partidas2+=1
        contador+=1
    
    if partidas1>partidas2:
        ganador = "jugador1"
    else:
        if partidas1 == partidas2:
            ganador = "empate"
        else:
            ganador = "jugador2"

    print (f'El ganador final es: {ganador}')

if __name__ == "__main__":
    main()
