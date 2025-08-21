##•	Día 4: Pedir dos números y mostrar el mayor.

a = int(input("Digite un numero1: "))
b = int(input("Digite un numero2: "))


if a > b:
    print(f"El numero mayor es {a}")
elif a == b:
    print(f"Los numeros son iguales")
else:
    print(f"El numero mayor es {b}")


#•	Día 5: Pedir una edad y decir si es mayor de edad (≥18).

edad = int(input("Digite su edad: "))
if edad >= 18:
    print(f"Usted es mayor de edad")
else:
    print(f"Usted no es mayor de edad")