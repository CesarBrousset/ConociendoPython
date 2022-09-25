lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
for valor in lista_1:
    if valor in lista_2 and valor not in lista_3:
        lista_3.append(valor)
               
print(lista_3)

print(type('asdas'))