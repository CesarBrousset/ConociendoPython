# def dividir(a, b):
#    if b == 0:
#        return None
#    return a / b


# print(dividir(4, 2) == 2)
# print(dividir(9, 3) == 3)
# print(dividir(2, 4) == 0.5)
# print(dividir(0, 8) == 0)
# print(dividir(8, 0) == None)
# print(dividir(-1, 0) == None)
# print(dividir(99, 0) == None)
while(True):
    try:
        n = float(input("Ingresar n:\n"))
        m = 4
        print(f"---> {n}/{m} = {n/m}".format(n, m, n/m))
        break
    except:
        print('ha ocurrido un error, introduce bien el número')  





