import math

def area(base, altura ,lados):
    area = (base * altura) / 2
    rel1 = altura/base
    rel2 = math.sqrt (3) /2
    print (rel1)
    print (rel2)

    if rel1 == rel2:
        tipo = "equilatero"
    else:
        if lados == 0:
            tipo = "escaleno"
        else:
            tipo = "isoceles"

    return area, tipo


def main():
    base = float(input('Ingresa la base del triángulo: '))
    altura = float(input('Ingresa la altura del triángulo: '))
    lados = int(input('Ingrese cuantos lados son iguales en el triangulo: '))
    areatriang, tipotriang = area(base, altura, lados)
    print (f'El area del triangulo es: {areatriang} y el tipo de triangulo es: {tipotriang}')

if __name__ == "__main__":
    main()
