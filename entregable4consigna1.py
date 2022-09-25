print("1. Para sumar")

print("2. Para restar el primero con el segundo")

print("3. Para multiplicar")

print("4. Para salir")

print("Seleccione una opcion, debe ingresar el número de opcion:")

(mi_numero) = int(input())

if (mi_numero == 1):
    print('elija otro numero: ')
    (mi_otro_numero) = int(input())
    suma_de_numeros = mi_numero + mi_otro_numero
    print(f'la suma de ambos es: {suma_de_numeros}') 
    
elif mi_numero == 2:
    print('elija otro numero: ')
    (mi_otro_numero) = int(input())
    resta_de_numeros = mi_numero - mi_otro_numero
    print(f'la diferencia entre el primero y el segundo es: {resta_de_numeros}')
    
elif mi_numero == 3:
    print('elija otro numero: ')
    (mi_otro_numero) = int(input())
    multiplo_de_numeros = mi_numero * mi_otro_numero
    print(f'la multiplicacion de ambos es: {multiplo_de_numeros}')
    
elif mi_numero == 4:
    False
    
    
else:
    print('la opción elegida no es correcta')