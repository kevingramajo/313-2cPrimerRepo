#PlayerHeight = float(input("Ingresar Altura: "))
#print(f"Tu altura es de {PlayerHeight}")
#if PlayerHeight< 1.60:
    #print("Eres Base")
#elif PlayerHeight<1.79:
    #print("Eres Escolta")
#elif PlayerHeight<1.99:
    #print("Eres Alero")
#else:
    #print("Eres Ala-Pivot o Pivot")

#notaParcial = int(input("Colocar Nota: "))
#if notaParcial <=3:
    #print(f"Desaprobado, tu nota es: {notaParcial}")
#elif notaParcial <=5:
    #print(f"Aprobado, tu nota es: {notaParcial}")
#elif notaParcial <=10:
    #print(f"Promocion, tu nota es: {notaParcial}")
#else:
    #print(f"Numero Incorrecto")

#Ejercicio Match
#destino=str(input("Indique su Lugar de Destino: "))
#estacion=str(input("Ahora Indique la estacion del Ano (Inviero,Verano,Otono o Primavera) "))
#match estacion:
    #case "Invierno":
        #if destino == "Bariloche":
            #print("Se Viaja")
        #else:
            #print("No Se Viaja")
    #case "Verano":
        #if destino == "Mar del Plata":
            #print("Se Viaja")
        #elif destino == "Cataratas":
            #print("Se viaja")
        #else:
            #print("No se viaja")
    #case "Primavera":
        #if destino == "Bariloche":
            #print("No se viaja")
        #else:
            #print("Se viaje")
    #case _:
        #print("Se Viaja")
print("===================================================================")
print("Bienvenido a Gotita S.A.")
print("===================================================================")
tipoCliente=str(input("Que tipo de Cliente sos: (Residencial, Comercial o Industrial) "))
consumo=int(input("Ingresar Cantidad de mts³ consumidos: "))
tarifaBase=7000
tarifatotal=(tarifaBase + consumo*200)
bonificacion=0
recargo=0
#El costo por metro cúbico (m³) de agua es de $200/m³.
if tipoCliente=="Residencial":
    if consumo<30:
        bonificacion=10
    elif consumo>80:
        recargo=15
if tipoCliente=="Residencial":
    if tarifatotal<35000:
        bonificacion+=5
elif tipoCliente=="Comercial":
    if consumo>300:
        bonificacion=12
    elif consumo>150:
        bonificacion=8
    elif consumo<50:
        recargo=5
elif tipoCliente=="Industrial":
    if consumo>1000:
        bonificacion=30
    elif consumo>500:
        bonificacion=20
    elif consumo<200:
        recargo=10
aplicacionBonif=(tarifatotal*bonificacion/100)
aplicacionRecargo=(tarifatotal*recargo/100)
total=(tarifatotal - aplicacionBonif + aplicacionRecargo)
iva=total * 21/100
print(f"Subtotal del consumo: {tarifatotal}")
print(f"Bonificacion: {bonificacion}")
print(f"Recargos: {recargo}")
print(f"Subtotal con Recargos o Bonif: {tarifatotal - aplicacionBonif + aplicacionRecargo}")
print(f"IVA Aplicado del 21%")
print(f"Total: {total + iva} ")
print(f"===================================================================")
