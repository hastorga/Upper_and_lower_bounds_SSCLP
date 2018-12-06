import numpy as np
import itertools
def leer_fichero():

    costo_apertura =[]
    capacidad =[]
    demanda = []
    costo_asignacion = []
    f = open("cap61.txt", "r")
    x = np.genfromtxt(itertools.islice(f, 0, 1, None), dtype=int)
    plantas = x[0]
    clientes = x[1]
    #Lectura de capacidad y costos de apertura de la planta i
    for i in range (plantas):
        step_0 = f.readline()[:-1].split(' ') # Leyendo linea
        capacity = float(step_0[0])
        open_cost = float(step_0[1])
        #print(capacity, ", ", open_cost)
        costo_apertura.insert(i,open_cost)
        capacidad.insert(i,capacity)
    #Lectura de la demanda de cada cliente j   
    step_0 = f.readline().split(' ')
    for j in range (clientes):
        demanda.insert(j,float(step_0[j]))
    #Para cada planta, existen costos de asignación de cliente, Matriz de 16x50
    for i in range (plantas):
        step_0 = f.readline().split(' ')
        for j in range(clientes):
                costo_asignacion.append([float(step_0[j])])
    print(costo_asignacion)
        # print (x[:,1]) imprime todos los datos de la columna 2 (inicia en 0)
        #print (x[0,:]) #imprime todos los datos de la fila 1
        # x = np.genfromtxt(itertools.islice(f_in, 2, 12, None), dtype=float)
leer_fichero()