#•	Día 6: Mostrar los números del 1 al 10 con un bucle for.

# que hace el bucle for? Recorrer elementos de un objeto iterable

for i in range (1,11):
    print(i)

#	Día 7: Mostrar la tabla de multiplicar de un número dado.

num1 = int(input("Ingresa un numero: "))

for i in range (1,11):
    print(str(i)+ " * " + str(num1)+ " = "+str(i*num1)+"\n")



# Pedir el número al usuario
num = int(input("Ingresa un número: "))

print(f"\nTabla de multiplicar del {num}:\n")

# Recorremos del 1 al 10
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
