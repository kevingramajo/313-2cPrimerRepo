#print("============================================================================")
#print("Numero Par e Impar")
#numeroSelecc=int(input("Seleccionar un Numero: "))
#if numeroSelecc % 2 == 0:
    #print("Es Par")
#else:
    #print("Es Impar")


#print("============================================================================")
#print("Anio Bisiesto?")
#def es_bisiesto(anio):
    #return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
#
##  Uso
#anio = 2028
#if es_bisiesto(anio):
    #print(f"El año {anio} es bisiesto.")
#else:
    #print(f"El año {anio} no es bisiesto.")

#print("============================================================================")
#print("Torre de Hanoi")
#def tower_of_hanoi(n, source, destination, helper):
	#if n==1:
		#print ("Move disk 1 from peg", source," to peg", destination)
		#return
	#tower_of_hanoi(n-1, source, helper, destination)
	#print ("Move disk",n," from peg", source," to peg", destination)
	#tower_of_hanoi(n-1, helper, destination, source)		
## n = number of disks
#n = 3
#tower_of_hanoi(n,' A','B','C')
#print("============================================================================")
#def es_primo(numero):
    #if numero < 2:
        #return False
    #for i in range(2, int(numero**0.5) + 1):
        #if numero % i == 0:
            #return False
    #return True
#
## Ejemplo de uso
#print(es_primo(2))  # True
#print(es_primo(6))  # False
#
#def generar_primos(hasta):
    #primos = []
    #for num in range(2, hasta + 1):
        #if es_primo(num):
            #primos.append(num)
    #return primos
#
## Ejemplo de uso
#print(generar_primos(20))  # [2, 3, 5, 7, 11, 13, 17, 19]

#print("============================================================================")
#print("Fibonacci")
#def fibonacci_generator(n):
    #a, b = 0, 1
    #for _ in range(n):
        #yield a
        #a, b = b, a + b
#
#print(list(fibonacci_generator(10)))  # Genera los primeros 10 números de Fibonacci

def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
print(f"El factorial de {numero} es: {factorial(numero)}")