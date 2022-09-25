#  Escribir una función que imprima el mensaje 'Hello World!'

saludo = 'Hello World!'

def saludar_al_mundo (saludo) -> str:
    print(saludo)
    return saludo

assert (saludar_al_mundo(saludo))

# Escribir una función que no reciba parámetros, 
# que en su cuerpo genere dos variables `mi_numero` y `mi_numero_2` con valores `10` y `20` y 
# que imprima la suma. El resultado debería ser:
print('*'*50)
mi_numero = 10
mi_numero_2 = 20

suma_total = mi_numero + mi_numero_2

def sumar_numeros():
    mi_numero + mi_numero_2
    return suma_total

print('la suma es: ', sumar_numeros())

# Escribir una función que reciba un parámetro (o argumento). 
# La función tiene que imprimir un mensaje reportando cuál es el valor del parámetro que recibió. 
# Por ejemplo, si recibe un `string` "esto es un texto", la función debe imprimir
print('*'*50)
dato = 55 

def identificar_dato (dato) -> str:
    print (f'he recibido como parametro: {dato}')
    if type(dato) == str:
        return 'esto es un texto' 
    elif type(dato) == int:
        return 'esto es un entero'
    elif type(dato) == list:
        return 'esto es una lista'
    elif type(dato) == tuple:
        return 'esto es una tupla'
    elif type(dato) == dict:
        return 'esto es un diccionario'
    elif type(dato) == bool:
        return 'esto es un booleano'
    else:
        return 'esto es un conjunto'      
    
dato = 'Hello World!'
print (identificar_dato(dato))

dato = 4560
print (identificar_dato(dato))

dato = [1, 2, 3, 4]
print (identificar_dato(dato))

dato = {'Cesar': 'cesar@coder.com: ', 'Minion': 'banana@coder.com'}
print (identificar_dato(dato))

dato = {1, 2, 3, 4, 5}
print (identificar_dato(dato))

dato = False
print (identificar_dato(dato))

#Dada la siguiente función:
#def mi_funcion(a, b):
   # x = a + b
   # return x
#i. Escribir un código que imprima la suma de dos números
#ii. Escribir un código que imprima la concatenación de dos strings 

print('*'*50)

def mi_funcion(dato, otro_dato):
    resultado = dato + otro_dato
    return resultado

print(mi_funcion(1, 5))
print(mi_funcion('hola ', 'mundo'))

#Escribir una función que reciba un número como argumento y 
# que imprima un mensaje donde se muestre el numero ingresado y 
# se explique si el número es par o impar. 
# Por ejemplo, si la función se llama mi_funcion entonces:

print('*'*50)

def identificar_si_es_par_o_impar(dato):
    if dato % 2 == 0:
        return f'el numero {dato} es par'
    else:
        return f'el numero {dato} es impar'
    
dato = 5
print(identificar_si_es_par_o_impar(dato))
dato = 10
print(identificar_si_es_par_o_impar(dato))
dato = 3
print(identificar_si_es_par_o_impar(dato))
dato = -2
print(identificar_si_es_par_o_impar(dato))
dato = 0
print(identificar_si_es_par_o_impar(dato))
dato = 35
print(identificar_si_es_par_o_impar(dato))

#Tomar la función definida en el punto anterior y 
# agregar el siguiente comportamiento: 
# si el argumento pasado a la misma no es un entero int entonces tiene que imprimir un mensaje 
# que diga "Argumento incorrecto" y explique el tipo de argumento recibido, por ejemplo:
#mi_funcion([1,23,4])
#>> "Argumento incorrecto: <class 'list'>"

#mi_funcion("4")
#
# >> "Argumento incorrecto: <class 'str'>"

print('*'*50)

def identificar_si_es_par_o_impar (dato):
    if type(dato) != int:
        return f'argumento incorrecto: {type(dato)}'
        
    if dato % 2 == 0:
        return f'el numero {dato} es par'
    else:
        return f'el numero {dato} es impar'    
    
    dato = 5
print(identificar_si_es_par_o_impar(dato))
dato = 10
print(identificar_si_es_par_o_impar(dato))
dato = 3
print(identificar_si_es_par_o_impar(dato))
dato = -2
print(identificar_si_es_par_o_impar(dato))
dato = 0
print(identificar_si_es_par_o_impar(dato))
dato = 35
print(identificar_si_es_par_o_impar(dato))
dato = (1, 2.5, 'kk')
print(identificar_si_es_par_o_impar(dato))
dato = 'cesar'
print(identificar_si_es_par_o_impar(dato))

#Implementar una función que reciba dos argumentos. 
# Si por lo menos uno de los dos argumentos no son strings str entonces que devuelva el valor False, 
# en cambio si los dos argumentos son strings, 
# que devuelva el conjunto de caracteres que consituyen ambos argumentos, en mayúsculas. 
# Por ejemplo, si la función se llama mi_funcion:
#res = mi_funcion(1, "bowie")
#print(f"el resultado es: {res}")
#>> el resultado es: False

#res = mi_funcion(1, [])
#print(f"el resultado es: {res}")
#>> el resultado es: False

#res = mi_funcion("a", "b")
#print(f"el resultado es: {res}")
#>> el resultado es: {'A', 'B'}

#res = mi_funcion("david", "bowie")
#print(f"el resultado es: {res}")
#>> el resultado es: {'V', 'B', 'O', 'D', 'E', 'A', 'I', 'W'}
print('*'*50)
print(set('cacaroto'.upper()))

def identificar_si_son_strings(dato, otro_dato):
    if type(dato) == str and type(otro_dato) == str: 
        return set((dato + otro_dato).upper())  
    else:
        return False


res = identificar_si_son_strings(1, 'Córdoba')
print(f'el resultado es: {res}')

res = identificar_si_son_strings ('kk', 'Cordoba')
print(f'el resultado es: {res}')

res = identificar_si_son_strings ('kk', 5)
print(f'el resultado es: {res}')

#Implementar 5 casos de test para una función que: 
# dado un texto (str), si el mismo tiene más de 10 caracteres, 
# tiene que devolver el mismo texto pero en mayúsculas. 
# En otro caso, si tiene un número par de caracteres tiene que devolver un conjunto
# con todos los caracteres utilizados y si tiene un numero impar de caracteres tiene que devolver
# el número de caracteres. Por ejemplo, si la función se llama mi_funcion, dos tests podrían ser:

#def mi_funcion(una_palabra):
#    return None

# Test 1
#resultado = mi_funcion("otorrinolaringologia")
#if resultado == "OTORRINOLARINGOLOGIA":
#    print("test correcto")
#else:
#    print("test incorrecto")

# Test 2
#resultado = identificar_del_string("casa")
#if resultado == {'s', 'c', 'a'}:
#   print("test correcto")
#else:
#    print("test incorrecto")

print('*'*50)

def identificar_del_string (dato):
    if len(dato) > 10:
        return dato.upper()
    else: 
        pass
    if len(dato) % 2 == 0:
       return set(dato)
    else:
        return len(dato) 
        
print(identificar_del_string('otorrinolaringologia'))
print(identificar_del_string('cesarea'))
print(identificar_del_string('casa'))        

# Test 2
resultado = identificar_del_string('casa')
if resultado == {'s', 'c', 'a'}:
   print("test correcto")
else:
    print("test incorrecto")
    
# Test 1
resultado = identificar_del_string("otorrinolaringologia")
if resultado == "OTORRINOLARINGOLOGIA":
    print("test correcto")
else:
    print("test incorrecto")
    
# Test 3
resultado = identificar_del_string("cesarea")
if resultado == 7:
    print("test correcto")
else:
    print("test incorrecto")
    
# Test 4    
resultado = identificar_del_string("carito")
if resultado == {'c', 'a','r', 'i', 't', 'o'}:
    print("test correcto")
else:
    print("test incorrecto")
    
# Test 5 
resultado = identificar_del_string("carito")
if resultado == 6:
    print("test correcto")
else:
    print("test incorrecto")    
#Implementar una función que pase todos los casos de tests escritos en el punto anterior.
