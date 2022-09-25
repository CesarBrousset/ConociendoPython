# Consigna: Realizar una función llamada año_bisiesto:

# Recibirá un año por parámetro
# Imprimirá “El año año es bisiesto” si el año es bisiesto
# Imprimirá “El año año no es bisiesto” si el año no es bisiesto
# Si se ingresa algo que no sea número debe indicar que se ingrese un número.

# Se recuerda que los años bisiestos son múltiplos de 4,
# pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
# Estos son algunos ejemplos de posibles respuestas:
# 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.


def identificar_si_el_año_es_bisiesto(dato: int):
    if type(dato) != int:
        return "debe ingresar imperiosamente un numero"
    else:
        pass
    if dato < 1582:
        return "el año bisiesto fue instaurado a partir de 1582"
    else:
        pass
    if (dato % 4 == 0 and dato % 100 != 0) or dato % 400 == 0:
        return f"El año {dato} es bisiesto"
    else:
        return f"El año {dato} no es bisiesto"


año = identificar_si_el_año_es_bisiesto(2012)
print(año)
año = identificar_si_el_año_es_bisiesto(2010)
print(año)
año = identificar_si_el_año_es_bisiesto(2000)
print(año)
año = identificar_si_el_año_es_bisiesto(1900)
print(año)
año = identificar_si_el_año_es_bisiesto(1500)
print(año)
año = identificar_si_el_año_es_bisiesto("roman")
print(año)
