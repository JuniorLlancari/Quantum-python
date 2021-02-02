mayor=0
menor=0
def instruccion(valor):
    global menor
    global mayor
    if(valor<menor):
        menor=valor
    if(valor>mayor):
        mayor=valor
def lectura():
    global menor
    global mayor
    valor1=input('Ingrese el primer valor : ')
    menor = int(valor1)        
    mayor = int(valor1)
    valor2=input('Ingrese el segundo valor : ')
    instruccion(int(valor2))
    valor3=input('Ingrese el tercer  valor : ')
    instruccion(int(valor3))
    valor4=input('Ingrese el cuarto  valor : ')
    instruccion(int(valor4))
    if(valor1==valor2 or valor1==valor3 or valor4==valor3):
        print(' Oh, Los valores tienen que ser distintos :)')
        lectura()
    else:
        print(f'El número mayor es {mayor}')
        print(f'El número menor es {menor}')
lectura()

