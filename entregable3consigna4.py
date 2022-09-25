print('coloque la cantidad requerida dentro de la lista, ó 0 para calcular la media')

numero = int(input())

mi_lista = []

while (numero != 0):

  print(f"Tu numero vale: {numero}\n")
  mi_lista += [numero]
  numero = int (input("Ingresar otro numero, 0 para salir\n"))

else:

  print(f"tu promedio es: {sum(mi_lista)/len(mi_lista)}")
    