def lectura():
    valor1=input('Ingrese el primer valor : ')
    valor2=input('Ingrese el segundo valor : ')
    valor3=input('Ingrese el tercer  valor : ')
    valor1=int(valor1)
    valor2=int(valor2)
    valor3=int(valor3)
    if(valor1==valor2 or valor1==valor3 ):
        print(' Oh, Los valores tienen que ser distintos :)')
        lectura()
    else:
        mayor=0
        menor=0
        if(valor1>valor2 and valor1>valor3):
            mayor=valor1
            if(valor3<valor2):
                menor=valor3
            else:
                menor=valor2
        if(valor2>valor1 and valor2>valor3):
            mayor=valor2
            if(valor3<valor1):
                menor=valor3
            else:
                menor=valor1
        if(valor3>valor1 and valor3>valor2):
            mayor=valor3
            if(valor1<valor3):
                menor=valor1
            else:
                menor=valor3
        print(f'El número mayor es {mayor}')
        print(f'El número menor es {menor}')
lectura()
