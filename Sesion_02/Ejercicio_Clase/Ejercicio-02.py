def convertir_moneda(tipo_de_cambio,moneda):
    monto=input(f'Ingresa el valor en {moneda}')
    monto_en_usd=round(float(monto)*tipo_de_cambio,2)
    print(f'El monto en USD es:'{monto_en_usd})


mensaje="""
Hola :
1 = Soles - Dolares
2 = Euros - Dolares
3 = COP - Dolares
"""

print (mensaje)
opcion=int(input("Ingrese opcion"))

if opcion==1:
    convertir_moneda(0.27,'Soles')
else if:
else if: