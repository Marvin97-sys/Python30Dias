# Condicionales

numero = int(input("Ingresa un numero: "))

if numero >0:
    print("El numero es positivo") # identacion, es el espacio que queda, sin eso ya no forma parte del if
elif numero ==0:
    print("El numero es cero")
else:
    print("El numero es negativo")

print("Fin del programa")


## CONDICIONALES COMBINADOS

edad = int(input("Ingresa edad: "))

if edad >0 and edad < 100: #operadores logicos en los condicionales. if 0<edad<100:
    print("Edad correcta")
    if edad >= 18: ##identacion
        print("Es mayor de edad")
else:
    print("Edad incorrecta")

## Ejercicio1
# Hacer un programa que pide 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))

if num1%2==0 and num2%2==0: ## si residuo es 0 dicho numero es par
    print("Ambos numeros son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print("Ambos numeros son impares")

#Ejercicio2
#Hacer un programa que pida 3 numeros y determine cual es el mayor

a = int(input("Ingresa numero 1: "))
b = int(input("Ingresa numero 2: "))
c = int(input("Ingresa numero 3: "))

if a >= b and a >= c:
    print(f"El primer numero: {a} es el numero mayor")
elif b >= a and b >= c:
    print(f"El segundo numero: {b} es el numero mayor")
elif c >= a and c >= b:
    print(f"El tercer numero: {c} es el numero mayor")

#Ejercico3
#hacer un programa que pida un caracter e indique si es una vocal o no
# vocales: a - e - i - o - u

voc = input("Ingresa un caracter: ").lower()
if voc == "a" or  voc == "e" or voc =="i" or voc == "o" or voc =="u":
    print("El caracter es una vocal")
else:
    print("El caracter no es vocal")