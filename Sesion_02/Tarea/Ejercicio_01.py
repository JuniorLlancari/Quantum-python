def lectura():
    valor1=input('Ingrese el primer valor : ')
    valor2=input('Ingrese el segundo valor : ')
    valor1=int(valor1)
    valor2=int(valor2)

    if(valor1>valor2):
        print(f'El valor {valor1} es mayor que {valor2}')
    if(valor1<valor2):
        print(f'El valor {valor2} es mayor que {valor1}')
    if(valor1==valor2):
        print('==Oh,Los valores tienen que ser distinto :)==')
        lectura()
lectura()
