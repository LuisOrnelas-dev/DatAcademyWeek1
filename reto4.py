import math

def cilindro():
    altura = float(input("Ingresa la altura del cilindro:\n"))
    radio = float(input("Ingresa el radio del cilindro:\n"))
    volumen = 2*math.pi*radio*altura
    print (f'El volumen del cilindro es: {volumen}')

def cubo():
    lado = float(input("Ingresa la medida del lado del cubo:\n"))
    volumen = 6*lado**2
    print (f'El volumen del cubo es: {volumen}')

def esfera():
    radio = float(input("Ingresa el radio de la esfera:\n"))
    volumen = 4*math.pi*radio**2
    print (f'El volumen de la esfera es: {volumen}')

def main():
    print('Ingrese el numero correspondiente a la figura a elegir para calcular su volumen\n')
    print('1) Cilindro')
    print('2) Cubo')
    print('3) Esfera')
    valor = (input())

    if valor == "1":
        cilindro()
    else: 
        if valor == "2":
            cubo()
        else:
            if valor == "3":
                esfera()


if __name__ == "__main__":
    main()
