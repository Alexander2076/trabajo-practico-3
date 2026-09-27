
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

# BORRAR PANTALLA
def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

# CARTEL DE GANASTE Y PERDISTE
def mensajeAnimado(mensaje, color):

    print(f"\n{color}{mensaje}", end="", flush=True)
    for i in range(3):
        time.sleep(0.4)
        print(f"{color}.{cerrarColor}", end="", flush=True)


# ANIMACION DE MENSAJE GANASTE Y PERDISTE
def animacion(jugador, mensaje, resultado):

    texto = f"{jugador} {mensaje}".center(50)
    if(resultado == "gano"): 
                winsound.PlaySound("sonidos/ganaste.wav", winsound.SND_ASYNC)
    else: 
                winsound.PlaySound("sonidos/perdiste.wav", winsound.SND_ASYNC)
            

    for i in range(20):

        if resultado == "gano":

            if i % 5 == 0:
                color = rojoNormal
            elif i % 5 == 1:
                color = verde
            elif i % 5 == 2:
                color = amarillo
            elif i % 5 == 3:
                color = azul
            else:
                color = violeta

        elif resultado == "perdio":

            if i % 5 == 0:
                color = rojoNormal
            elif i % 5 == 1:
                color = rojoIntenso
            elif i % 5 == 2:
                color = rojoError
            elif i % 5 == 3:
                color = rojoNormal
            else:
                color = rojoIntenso
        print(f"\r{color}{texto}{cerrarColor}", end="")
        time.sleep(0.1)

    print()

# CERRAR JUEGOS
def cerrarJuego(jugador, juego):
    if (jugador == ""): 
        cerrar = str(input(f"\nDesea jugar {juego}? (s/n)  ")).lower().strip()
        while (cerrar != "n" and cerrar != "s"):
            cerrar = str(input(f"{rojoError}\nError - Ingrese s/n:{cerrarColor} "))
    else: 
        cerrar = str(input(f"\n{jugador} desea seguir jugando {juego}? (s/n)  ")).lower().strip()
        while (cerrar != "n" and cerrar != "s"):
            cerrar = str(input(f"{rojoError}\nError - Ingrese s/n :{cerrarColor} "))
    return cerrar

def validarNombre(mensaje):
    nombre = str(input(f"\n{mensaje}").strip())
    while len(nombre) < 3:
        nombre = str(input(f"\n{rojoError}Error - Ingrese nuevamente su nombre, al menos 3 caracteres: {cerrarColor}")).strip()
    borrarPantalla()
    return nombre

ArcFisJug = "jugadores.dat"

if not os.path.exists(ArcFisJug):

    ArcLogJug = open(ArcFisJug, "w+b")

    print("creado")

else:

    ArcLogJug = open(ArcFisJug, "r+b")

    print("ya existe")

