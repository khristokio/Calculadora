


numero1 = int(input("Primer número"))
numero2 = int(input(" Segundo número"))

eleccion = 0

while eleccion != 6:
    print("""
    Indique la operación
    
    1) sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Cambiar los números
    6) salir de la calculadora

    """)
    eleccion = int(input() )

    if eleccion == 1:
        print(" ")
        print("resultado:",numero1," + ",numero2," = ",numero1+numero2)
    elif eleccion == 2:
        print(" ")
        print("resultado:",numero1," - ",numero2," = ",numero1-numero2)    
    elif eleccion == 3:
        print(" ")
        print("resultado:",numero1," x ",numero2," = ",numero1*numero2)
    elif eleccion == 4:
        print(" ")
        print("resultado:",numero1," / ",numero2," = ",float(numero1/numero2)) 
    elif eleccion == 5:
        numero1 = int(input("Introduzca primer número:") )
        numero2 = int(input("Introduzca segundo número:") )
    elif eleccion == 6:
        print("Hasta pronto")

