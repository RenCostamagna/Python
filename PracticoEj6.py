def carga():
    global promedio
    sumaNotas = 0.00
    for i in range (5):
        nota[i] = int(input('Ingrese nota: '))
        sumaNotas += nota[i]
        promedio = sumaNotas/5

def aprobados():
    for i in range (5):
        if nota[i] > promedio:
            print('El alumno ',i,' tiene nota mayor al promedio')


nota = [0] * 5
carga()
aprobados()