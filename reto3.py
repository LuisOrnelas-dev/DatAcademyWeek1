import math

def conversion(valor, cantidad):
    if valor == "1":
        resultado = str(cantidad) + " millas es igual a " +str(cantidad*1.609344)+ " km"
    else:
        if valor == "2":
            resultado = str(cantidad) + " km es igual a " +str(cantidad/1.609344)+ " millas"
    return resultado


def main():
    valor = (input('Ingrese "1" para convertir de millas a kilómetro \nIngrese "2" para convertir de kilómetros a millas \n'))
    cantidad = float(input('Ingrese cantidad a convertir\n'))
    resultado = conversion(valor, cantidad)
    print (resultado)

if __name__ == "__main__":
    main()
