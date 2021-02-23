class Proceso:

    def __init__(self):
        pass
           
    def retroceso(self,cadena):
        nueva_cadena=""
        for letra in cadena:
            nueva_cadena+=letra
            if letra=='#':
                nueva_cadena = nueva_cadena[:-2]
        print(nueva_cadena)
               
cadena=input("Ingrese la cadena : ")
cadena=str(cadena)
obj=Proceso()
obj.retroceso(cadena)
