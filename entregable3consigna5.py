print('escriba un número del 0 al 9')

mi_lista = [1, 3, 6, 9]
numero = int(input())

while numero > 10:
    print ('es incorrecto\n ingrese otro número')
    numero = int(input())
else:
    print('es correcto')
    
for numero in mi_lista:
    print('coloque el número nuevamente para comprobar que se encuentra en la lista')
    mi_lista = [1, 3, 6, 9]
    numero = int(input())
    if numero in mi_lista:
        print(True)
        break
    else:
        print(False)
        break
    

