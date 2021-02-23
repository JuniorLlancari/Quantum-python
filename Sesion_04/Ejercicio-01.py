
import random
def generar_pass():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    simbolos = ['!', '@', '$', '%', '(', ')', '/', '&']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []
    #print(caracteres)


    for i in  range(16):
        # Escoge uno aleatoriamente
        randon_element=random.choice(caracteres)
        contrasena.append(randon_element)
    #Coje elmento por elemento
    pass_final="".join(contrasena)
    print(pass_final)

generar_pass()