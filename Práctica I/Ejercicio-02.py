
longitud=input("Ingrese la longitud :")
ancho=input("Ingrese el ancho :")
longitud=float(longitud)
ancho=float(ancho)

if(ancho==longitud):
    print(f"El área del poligono es : {pow(ancho, 2)}")
else:
    print(f"El perimetro del poligono es : {longitud*2+ancho*2}")




