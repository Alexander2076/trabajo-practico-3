
import os, pickle, random as aleatorio, time, winsound

# ================= REGISTROS ================================
class categoria:
    def __init__(self):
        self.nroCategoria = 0
        self.nombreCategoria = "".ljust(30, " ")
        self.pregunta = "".ljust(200, " ")
        self.estado = "A" #Activa o Inactiva

class opcion:
    def __init__(self):
        self.nroCategoria = 0
        self.nroOpcion = 0
        self.objeto = "".ljust(100, " ")
        self.valor = 0

class jugador:
    def __init__(self):
        self.nombre = "".ljust(30, " ")
        self.credito = 10000
        self.juegos = matriz(2,4,0)

# ================= FUNCIONES Y PROCEDIMIENTOS GENERALES =================

# CREAR MATRIZ
def matriz(filas, columnas, tipo):
    matriz = [tipo] * filas

    for i in range(filas):
        matriz[i] = [tipo] * columnas
    
    return matriz

ArcFisJug = "jugadores.dat"

if not os.path.exists(ArcFisJug):

    ArcLogJug = open(ArcFisJug, "w+b")

    print("creado")

else:

    ArcLogJug = open(ArcFisJug, "r+b")

    print("ya existe")

