def carga(numero):
    for i in range (5):
        numero[i] = float(input('Ingresa un numero real: '))

def suma(numero):
    num = 0    
    for i in range (5):
        if (numero[i] % 2) == 0:
            num = num + numero[i] 
        return num
    
def sumapares(numero):
    num = 0    
    for i in range (5):
        if (numero[i] % 2) == 0:
            num = num + numero[i] 
    return num



arreglo = [0] * 5
carga(arreglo)
#total = suma(arreglo)
total = sumapares(arreglo)
print(total)