print("Hola mundo\nMi nombre es Rodrigo")


numero = 10.56

print(numero)
print(type(numero))


cadena = "Estoy"
print(cadena)
print(type(cadena))

valor = False
print(valor)
print(type(valor))


num1= 10
num2 = 6.7
resultado = (num1 + num2) * 10 /6

print("El resultado es: ",resultado)

#tipado numerico. de cualquier tipo de dato a cualquier tipo de dato#
'''Prueba de comentarios en python '''

valor = 10
print(valor)

valor = "Alejandro"
print(valor)

#### operadores aritmeticos

resultado = 10 + 5
print("El resultado es: ",resultado)

resultado = 10 - 5
print("El resultado es: ",resultado)

#suma
num1 = 10
num2 = 20
resultado = num1 + num2
print("El resultado es: ",resultado)

#resta
num1 = 10
num2 = 20
resultado = num1 - num2
print("El resultado es: ",resultado)

#multi
num1 = 10
num2 = 20
resultado = num1 * num2
print("El resultado es: ",resultado)

# division
num1 = 10
num2 = 3
resultado = num1 / num2 #division entera //
print("El resultado es: ",resultado)

# modulo
num1 = 10
num2 = 3
resultado = num1 % num2 #retorna residuo
print("El resultado es: ",resultado)


# exponenciasion
num1 = 2
num2 = 5
resultado = num1 ** num2
print("El resultado es: ",resultado)


# expresion mat

resultado = 3**3 * (13/5 -(2*4))
print("El resultado es: ",resultado)


## operadores relacionales
#relacion entre 2 valores
#compara valores entre si (verdadero o falso)
#tienen mismo nivel de prioridad en su evaluacion
#menor prioridad que los aritmeticos
#mayor menor que etc


resultado = 10 < 20
print(resultado)

resultado = 10 > 20
print(resultado)

resultado = 10 == 20
print(resultado)

resultado = 10 != 20
print(resultado)

resultado = 10 <= 20
print(resultado)

resultado = 10 >= 20
print(resultado)

#combinar
a = 10
b = 20
c = 30

resultado = a+b == c # !=
print(resultado)


##OPERADORES LOGICOS
#Permite construir expre logicas, se obtiene como resultado booleanos
# AND (conjuncion) . Or (disyuncio) . Negacion Not
#buscar cuadros

#Prioridad
# 1.NOT
# 2.AND
# 3.OR

#Prioridad de los operadores en general
# 1. ()
# 2. **
# 3. *,/,mod, not
# 4. +,-,and
# 5. >,<,==,>=,<=,!=,or

a= 10
b = 15
c = 20

resultado = ((a<b) and (b<c))
print(resultado)

resultado = ((a>b) and (b<c))
print(resultado)

resultado = ((a>b) or (b<c))
print(resultado)

resultado = not((a>b) or (b<c))
print(resultado)


### OPERADORES DE ASIGNACION
# sirven para cortar el codigo

a = 0

a += 5 # suma en asignacion
a -= 2 # resta en asignacion
a *= 3 # multiplicacion en asignacion
a /= 3 # division en asignacion
a **=2 # potencia en asignacion
a %= 2 # modulo en asignacion

print(a)


### SALIDAS DE DATOS POR CONSOLA

nombre= "Rodrigo"
edad = 28

print("Hola", nombre, "tienes" , edad, "años")

print("Hola {} tienes {} años".format(nombre, edad))

print(f"Hola {nombre} tienes {edad} años")


### ENTRADA DE DATOS

##nombre2 = input("Digite su nombre: ")## guarda el dato tipo cadena
###print(f"Hola {nombre2}")

###numero = int(input("Digite su numero: "))## guarda el dato tipo cadena
###print(f"El numero es {numero+1}")

###numero = float(input("Digite su numero: "))## guarda el dato tipo cadena
###print(f"El numero es {numero}")


###FUNCIONES INTEGRADAS

n = str(10)
d = bin (10)
e = hex(10)
f= int("0b1010",2)
g= int("0xa",16)
print(n)
print(d)
print(e)
print(f)
print(g)

h = abs(-8) #valor absoluto
j = round(5.6) #redondea
k = len("Rodrigo")
print(h)
print(j)
print(k)


###EJERCICIOS 1 : Capitulo 1 Elementos BASICOS

# Escribir la sig expresion en forma de expresion algoritmica



###EJERCICIOS 4 : Capitulo 1 Elementos BASICOS

# hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia

import math

radio = float(input("Radio: "))

area= math.pi * radio ** 2
longitud = 2 * math.pi * radio

print(f"El area es: {area:.2f}") #imprimir resultados flotantes
print(f"El longitud es: {longitud:.2f}")

###Uma tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto
#debera pagar finalmente por su compra

precio = float(input("Digite el precio del producto: "))

descuento = precio * 0.15
precio_final = precio - descuento

print(f"El precio final es: ${precio_final:.2f}")

