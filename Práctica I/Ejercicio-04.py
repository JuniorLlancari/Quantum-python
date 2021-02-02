 def lectura():
    valor=input("Ingrese el numero de mes :")
    valor=int(valor)
    if(valor<=12 and valor>=1):
        if(valor<=3 and valor>=1):
            print("Es parte del Primer Trimestre ")
        if(valor<=6 and valor>=4):
            print("Es parte del Segundo Trimestre ")
        if(valor<=9 and valor>=7):
            print("Es parte del Tercer Trimestre ")
        if(valor<=12 and valor>=10):
            print("Es parte del Cuarto Trimestre ")
    else:
        print("Valor invalidado,Vuelva a ingresar :")
        lectura()
lectura()