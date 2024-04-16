def carga():
    for i in range (5):
        arreglo[i] = str(input("Ingrese un caracter: "))

def selecciono():
    for i in range (5):
        if arreglo[i] != "*":
            print(arreglo[i]," esta en la posicion",i+1)

arreglo = [" "] * 5
carga()
selecciono()
