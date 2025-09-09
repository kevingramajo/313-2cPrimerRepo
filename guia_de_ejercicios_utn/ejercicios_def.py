#Enunciado:
#Escribí una función que reciba base y altura, y devuelva el área.
#Datos por consola un argumento por defecto =10

#def devolverArea(base=10, altura=10):
    #area=(base*altura)/2
    #return area
#base=int(input("Ingresar Base: "))
#altura=int(input("Ingresar Altura: "))
#print(f"Tu Area es de: {devolverArea(base, altura)} (por defecto =10)")

#"""Nivel Intermedio
#Función que devuelva suma, resta y multiplicación
#
#Enunciado:
#Escribí una función que reciba dos números y devuelva los tres resultados: suma, resta y multiplicación."""
#numA=int(input("Colocar un numeroA: "))
#numB=int(input("Colocar un numeroB: "))
#def calculadora(numA, numB):
    #suma=numA+numB
    #resta=numA-numB
    #multiplicacion=numA*numB
    #return(suma,resta,multiplicacion)
#suma,resta,multiplicacion= calculadora(numA,numB)
#
#print(f"La suma de {numA} + {numB} es: {suma}")
#print(f"La resta de {numA} - {numB} es: {resta}")
#print(f"La multiplicacion de {numA} x {numB} es: {multiplicacion}")

"""
Enunciado:
Escribí una función que reciba cualquier cantidad de números y los suma los parametros por consola.

Ayuda: pedir al usuario cuantos numeros cargar, luego usar ese valor para iterar"""


def funcion_1():
    suma=0
    contador=0
    while True:
        numero=int(input("Ingrese un Numero: "))
        if numero>=0:
            suma +=numero
            contador +=1
        else:
            negativos +=numero
            contador +=1

        continuar=input("Quiere continuar agregando Numeros [SI] S/N [NO]?")
        if continuar == "n":
            return suma, contador
        
suma,contador = funcion_1()
        
print(f"La suma de los numeros ingresados es: {suma}")
print