class libro():
    def __init__(self):
        self.codigo = 0
        self.nombreLibro = " "
        self.anoEdicion = 0

def validar(max,min,valor):
    try:    
        if valor <= max and valor >= min:
            return True
        else:
            return False
    except:
        return False
    
def ordenoCarga(array):
    for k in range (0,2):
        for j in range (k+1,3):
            if array[k].codigo > array[j].codigo and array[j].codigo != 0:
                aux = array[j]
                array[j] = array[k]
                array[k] = aux
                

def carga():
    codigo = int(input("Ingrese 1 para continuar 0 para salir"))
    if codigo != 0:
        for i in range (3):
            arreglo[i].codigo = int(input('Ingrese codigo de alumno: '))
            arreglo[i].nombreLibro = input('Ingrese nombre del libro: ')
            anoEdicion = int(input('Ingrese ano de edicion'))
            while validar(2005,0, anoEdicion) == False:
                anoEdicion = int(input('Ingrese ano de edicion valido'))
            arreglo[i].anoEdicion = anoEdicion
            ordenoCarga(arreglo)

def muestro():
    for i in range (3):
        print('Codigo: ', arreglo[i].codigo)
        print('El nombre del libro: ', arreglo[i].nombreLibro)
        print('Ano del libro: ', arreglo[i].anoEdicion)

arreglo = [None] * 3
for i in range (3):
    arreglo[i] = libro() 
carga()
muestro()
