
def main():
    liminf = int (input('Ingresa un límite inferior:\n'))
    limsup = int (input('Ingresa un límite superior:\n'))
    num = int (input('Ingresa un numero a comparar:\n'))


    while (num<liminf) or (num>limsup):
        num = int (input('Ingresa un numero a comparar'))

    print(f'Numero dentro del rango: {num}')

if __name__ == "__main__":
    main()
