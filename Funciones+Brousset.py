#EJERCICIO 1 //
#CONSIGNA:
#Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura.
# Calcula el área de un rectángulo de 15 de base y 10 de altura.
#🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.
b = 15
h = 10
def area_rectangulo(b, h):
    area = b * h
    return area

cancha_de_talleres = area_rectangulo(b, h)
print(cancha_de_talleres)
    
#EJERCICIO 2 //
#CONSIGNA:
#Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio.
# Calcula el área de un círculo de 5 de radio.
#🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y 
# multiplicando el resultado por el número pi. 
# Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.
import math
r = 5
def area_circulo(r):
    area = (r**2) * math.pi 
    return area

pelota = area_circulo(r)
print(pelota)

#EJERCICIO 3 //
#CONSIGNA:
#Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
#1 - Si el primer número es mayor que el segundo, debe devolver 1.
#2 - Si el primer número es menor que el segundo, debe devolver -1.
#3 - Si ambos números son iguales, debe devolver un 0.
#Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(un_numero, otro_numero):
    if un_numero > otro_numero:
        return 1
    else:
        pass
    if un_numero < otro_numero:
        return -1
    else:
        return 0
    
primer_caso = relacion(5, 10)
print(primer_caso)
segundo_caso = relacion(10, 5)
print(segundo_caso)
tercer_caso = relacion(5, 5)    
print(tercer_caso)

#EJERCICIO 4 //
#CONSIGNA:
#Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
#🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
#Comprueba el punto intermedio entre -12 y 24
first_number = -12
second_number = 24

def intermedio(first_number, second_number):
    promedio = (first_number + second_number) / 2
    return promedio

average = intermedio(first_number, second_number)
print(average)

#EJERCICIO 5 //
#CONSIGNA:
#Realizá una función llamada recortar() que reciba tres parámetros.
#El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior.
#La función tendrá que cumplir lo siguiente:
#1 - Devolver el límite inferior si el número es menor que éste.
#2 - Devolver el límite superior si el número es mayor que éste.
#3 - Devolver el número sin cambios si no se supera ningún límite.
#Comprueba el resultado de recortar 15 entre los límites 0 y 10

def recortar(a, b, c):
    if a < b:
        return b
    else:
        pass
    if a > c:
        return c
    else:
        return a

porciones = recortar(15, 0, 10)
print(porciones)

#EJERCICIO 6 //
#CONSIGNA:
#Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.
#La primera con los números pares, y la segunda con los números impares:
#🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()
#Por ejemplo:
#pares, impares = separar([6,5,2,1,7])
#print(pares)   # valdría [2, 6]
#print(impares)  # valdría [1, 5, 7]

def separar(lista):
    even = []
    odd = []
    for element in lista:
        if (element % 2 == 0):
            even.append(element)
        else:  
            odd.append(element)
    print (sorted(even))
    print (sorted(odd))

list = [6,5,2,1,7]
separar(list)      



