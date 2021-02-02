def lectura():
    valor=input('Ingrese el valor : ')
    valor=int(valor)
    if(valor%2==0):
        print(f'El valor {valor} es un numero par')
    else:
        print(f'El valor {valor} no es un numero par')

lectura()


