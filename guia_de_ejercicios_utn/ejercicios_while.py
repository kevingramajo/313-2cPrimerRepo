#print(f"=============================================")
#print(f"1.Mostrar 10 repeticiones de números ascendentes desde el 1 al 10")
#a= 0
#while a <=10:
    #print(a)
    #a +=1
#print(f"=============================================")
#print(f"2.Mostrar 10 repeticiones de números descendentes desde el 10 al 1")
#b= 10
#while b >=0:
    #print(b)
    #b -=1
#print(f"=============================================")
#print(f"3.Mostrar la suma de los números desde el 1 hasta el 10")
#numero = 1
#suma = 0
#
#while numero <= 10:
    #suma += numero
    #print("Suma hasta", numero, "=", suma)
    #numero += 1
#print("La suma de los números del 1 al 10 es:", suma)

#print(f"=============================================")
#print(f"4.Mostrar la suma de los números pares desde el 1 hasta el 10")
#numero = 2
#suma = 0
#
#while numero <= 10:
    #suma += numero
    #print("Suma numeros Par", numero, "=", suma)
    #numero += 2

#print(f"=============================================")
#print(f"5-Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla")
#a=int(input("Ingresar un Numoro A: "))
#b=int(input("Ingresar un Numero B: "))
#c=int(input("Ingresar un Numero C: "))
#d=int(input("Ingresar un Numero D: "))
#e=int(input("Ingresar un Numero E: "))
#promedio= float((a+b+c+d+e)/5)
#print(f"La suma de los numeros ingresados es de: {a} + {b} + {c} + {d} + {e} ")
#print(f"Su promedio es de: {promedio}")

#print(f"=============================================")
#print(f"6-Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.")
#suma=0
#contador=0
#
#while True:
    #numero=int(input("Ingrese un Numero "))
    #suma +=numero
    #contador +=1
#
    #continuar=input("Quiere continuar agregando Numeros [SI] S/N [NO]?")
    #if continuar == "n":
        #break
#promedio= (suma/contador)
#if contador >0:
    #print(f"La suma de los numeros ingresados es de: {suma} ")
    #print(f"Su promedio es de: {promedio}")

#print(f"=============================================")
#print(f"7-Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos")
#suma=0
#negativos=0
#contador=0
#
#while True:
    #numero=int(input("Ingrese un Numero: "))
    #if numero>=0:
        #suma +=numero
        #contador +=1
    #else:
        #negativos +=numero
        #contador +=1
#
    #continuar=input("Quiere continuar agregando Numeros [SI] S/N [NO]?")
    #if continuar == "n":
        #break
#print(f"La suma de sus numeros Positivos es: {suma}")
#print(f"El producto de sus numeros Negativos es: {negativos}")

print(f"=============================================")
print(f"8-Ingresar 10 números enteros. Determinar el máximo y el mínimo.")
contador=0
#Revisar como hacer una lista junto con el input
while True:
    numero=float(input("Ingrese un Numero: "))
    lista=[float(numero)]
    contador +=1
    numero += lista
    if contador == 10:
        break

maximo= max(numero)
minimo= min(numero)
print(f"Maximo: {maximo}, Minimo: {minimo}")
