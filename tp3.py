
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

# VARIABLES COLOR
def color():
    global verde, rojoError, rosa, cerrarColor, amarillo, violeta, purpura, azul, rojoNormal, rojoIntenso, blanco, negro
    rojoError = "\033[41m"
    rojoNormal = "\033[31m"
    rojoIntenso = "\033[1;38;5;196m"
    verde = "\033[1;32m"
    amarillo = "\033[1;33m"
    violeta = "\033[1;38;5;93m"
    rosa = "\033[1;38;5;200m"
    azul = "\033[1;34m"
    blanco = "\033[47m"
    negro = "\033[30m"
    cerrarColor = "\033[0m"

ArcFisJug = "jugadores.dat"

if not os.path.exists(ArcFisJug):

    ArcLogJug = open(ArcFisJug, "w+b")

    print("creado")

else:

    ArcLogJug = open(ArcFisJug, "r+b")

    print("ya existe")

