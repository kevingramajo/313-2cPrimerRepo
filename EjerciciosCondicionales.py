PlayerHeight = float(input("Ingresar Altura: "))
print(f"Tu altura es de {PlayerHeight}")
if PlayerHeight< 1.60:
    print("Eres Base")
elif PlayerHeight<1.79:
    print("Eres Escolta")
elif PlayerHeight<1.99:
    print("Eres Alero")
else:
    print("Eres Ala-Pivot o Pivot")