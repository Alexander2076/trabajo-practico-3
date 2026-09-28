
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

# VALIDAR NOMBRE
def validarNombre(mensaje):
    nombre = str(input(f"\n{mensaje}").strip())
    while len(nombre) < 3:
        nombre = str(input(f"\n{rojoError}Error - Ingrese nuevamente su nombre, al menos 3 caracteres: {cerrarColor}")).strip()
    borrarPantalla()
    return nombre

def buscarNombre(nombre, registro, parametro):
    global arcLogJug, arcFisJug

    index = 0
    tam = os.path.getsize(arcFisJug)
    arcLogJug.seek(0,0)

    if tam > 0:
        registro = pickle.load(arcLogJug)
        while arcLogJug.tell() < tam and getattr(registro, parametro) != nombre:
            index = arcLogJug.tell()
            registro = pickle.load(arcLogJug)
        if getattr(registro, parametro) == nombre:
            return index
        else:
            return -1
    else:
        return -1
    
def jugadorActual(registro, pos): 
    global arcLogJug
    arcLogJug.seek(pos, 0)
    registro = pickle.load(arcLogJug)
    jugador = registro.nombre

    return jugador

def altaJugador(registro, nombre):
    global arcLogJug
    arcLogJug.seek(0, 2)
    registro = jugador()
    registro.nombre = nombre
    formatJugador(registro)
    pickle.dump(registro, arcLogJug)
    arcLogJug.flush()

def formatJugador(registro):
    registro.nombre = registro.nombre.ljust(30, " ")
    registro.credito = str(registro.credito).ljust(5, " ")
    for i in range(2):
        for j in range(4):
            registro.juegos[i][j] = str(registro.juegos[i][j]).ljust(4, " ")

def abrirArchivo(ruta):
    if not os.path.exists(ruta):
        archivo = open(ruta, "w+b")
        print("Archivo creado")
    else:
        archivo = open(ruta, "r+b")
        print("El archivo ya existe")
    return archivo

# =============== MENU PRINCIPAL =================
def menuop():
    borrarPantalla()
   
    winsound.PlaySound("sonidos/menu.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

    borrarPantalla()
    
    print(f"{azul}╔════════════════════════════════════╗")
    print(f"{azul}║            🎰  MENU 🎰             ║")
    print(f"{azul}╚════════════════════════════════════╝{cerrarColor}")

    print(f"{violeta}A. Mayor o Menor.{cerrarColor}")
    print(f"{rosa}B. Numero Secreto.{cerrarColor}")
    print(f"{amarillo}C. BlackJack.{cerrarColor}")
    print(f"{azul}D. Par o Impar.{cerrarColor}")
    print(f"{verde}E. Reporte.{cerrarColor}")
    print(f"{rojoIntenso}S. Fin del PROGRAMA{cerrarColor}")
    
    print(f"{azul}{'═'*36}{cerrarColor}")

def menu(): 
    
    borrarPantalla()
    opc = ""
    while (opc != "s"):
        menuop()

        opc = str(input("\nIngrese la letra del menu: ")).lower()
        while (opc<"a" or opc>"e" and opc!="s"):
            opc = str(input(f"{rojoError}\nIngreso invalido - reintente{cerrarColor}"))

        match opc:
            case "a":
                winsound.PlaySound(None, winsound.SND_ASYNC)
                juego1()
            case "b":
                winsound.PlaySound(None, winsound.SND_ASYNC)
                juego2()
            case "c":
                winsound.PlaySound(None, winsound.SND_ASYNC)
                juego3()
            case "d":
                winsound.PlaySound(None, winsound.SND_ASYNC)
                juego4()
            case "e":
                winsound.PlaySound(None, winsound.SND_ASYNC)
                reportes()
            case "s":
                salir()

# =============== ADMINISTRACION DE JUEGO =================
def pantallaAdmin():
    borrarPantalla()
    print(f"{rojoIntenso}╔════════════════════════════════════╗")
    print(f"{rojoIntenso}║        ⚙️ ADMINISTRACION ⚙️        ║")
    print(f"{rojoIntenso}╚════════════════════════════════════╝{cerrarColor}")

    print(f"{verde}A. Administrar Categorias.{cerrarColor}")
    print(f"{verde}B. Administrar Opciones.{cerrarColor}")
    print(f"{azul}C. Volver al menu principal.{cerrarColor}")

    print(f"{rojoIntenso}{'═'*36}{cerrarColor}")

def admin():
    borrarPantalla()
    opc = ""
    while (opc != "c"):
        pantallaAdmin()

        opc = str(input("\nIngrese la letra del menu: ")).lower()
        while (opc<"a" or opc>"c"):
            opc = str(input(f"{rojoError}\nIngreso invalido - reintente{cerrarColor}"))

        match opc:
            case "a":
                borrarPantalla()
                administrarCategorias()
            case "b":
                borrarPantalla()
                administrarOpciones()
            case "c":
                borrarPantalla()
                menu()

def pantallaAdminCategorias():
    borrarPantalla()
    print(f"{rojoIntenso}╔════════════════════════════════════╗")
    print(f"{rojoIntenso}║        ⚙️ ADMINISTRACION ⚙️        ║")
    print(f"{rojoIntenso}╚════════════════════════════════════╝{cerrarColor}")

    print(f"{verde}a. Alta.{cerrarColor}")
    print(f"{verde}b. Modificacion.{cerrarColor}")
    print(f"{verde}c. Baja.{cerrarColor}")
    print(f"{azul}d. Volver al menu anterior.{cerrarColor}")

    print(f"{rojoIntenso}{'═'*36}{cerrarColor}")

def administrarCategorias():
    borrarPantalla()
    opc = ""
    while (opc != "d"):
        pantallaAdminCategorias()

        opc = str(input("\nIngrese la letra del menu: ")).lower()
        while (opc<"a" or opc>"d"):
            opc = str(input(f"{rojoError}\nIngreso invalido - reintente{cerrarColor}"))

        match opc:
            case "a":
                borrarPantalla()
                altaCategoria()
            case "b":
                borrarPantalla()
                modificarCategoria()
            case "c":
                borrarPantalla()
                bajaCategoria()
            case "d":
                borrarPantalla()
                admin()

def pantallaAdminOpciones():
    borrarPantalla()
    print(f"{rojoIntenso}╔════════════════════════════════════╗")
    print(f"{rojoIntenso}║        ⚙️ ADMINISTRACION ⚙️        ║")
    print(f"{rojoIntenso}╚════════════════════════════════════╝{cerrarColor}")

    print(f"{verde}a. Alta.{cerrarColor}")
    print(f"{verde}b. Consulta.{cerrarColor}")
    print(f"{azul}d. Volver al menu anterior.{cerrarColor}")

    print(f"{rojoIntenso}{'═'*36}{cerrarColor}")

def administrarOpciones():
    borrarPantalla()
    opc = ""
    while (opc != "d"):
        pantallaAdminOpciones()

        opc = str(input("\nIngrese la letra del menu: ")).lower()
        while (opc<"a" or opc>"d"):
            opc = str(input(f"{rojoError}\nIngreso invalido - reintente{cerrarColor}"))

        match opc:
            case "a":
                borrarPantalla()
                altaOpcion()
            case "b":
                borrarPantalla()
                consultaOpcion()
            case "d":
                borrarPantalla()
                admin()

# =============== ADMINISTRACION DE CATEGORIAS =================
def validarPregunta(nombre):
    pregunta = str(input(f"\nIngrese la pregunta para la categoría '{nombre}': ")).strip()
    if not pregunta.startswith("¿"):
        pregunta = "¿" + pregunta
    if not pregunta.endswith("?"):
        pregunta = pregunta + "?"
    borrarPantalla()
    return pregunta

def formatoCategoria(regCategoria):
    regCategoria.nroCategoria = str(regCategoria.nroCategoria).ljust(3, " ")
    regCategoria.nombreCategoria = regCategoria.nombreCategoria.ljust(30, " ")
    regCategoria.pregunta = regCategoria.pregunta.ljust(200, " ")

def altaCategoria():
    borrarPantalla()
    print(f"{verde}╔════════════════════════════════════╗")
    print(f"{verde}║        ⚙️ ALTA CATEGORIA ⚙️        ║")
    print(f"{verde}╚════════════════════════════════════╝{cerrarColor}")

    global arcLogCat, arcFisCat

    nombre = validarNombre("Ingrese el nombre de la categoría: ")
    
    regCategoria = categoria()

    pos = buscarNombre(nombre, regCategoria, "nombreCategoria")

    if pos == -1:
        arcLogCat.seek(0, 2)
        regCategoria.nroCategoria = regCategoria.nroCategoria + 1
        regCategoria.nombreCategoria = nombre
        pregunta = validarPregunta(nombre)
        regCategoria.pregunta = pregunta
        formatoCategoria(regCategoria)
        pickle.dump(regCategoria, arcLogCat)
        arcLogCat.flush()

        print(f"{verde}\nCategoría '{nombre}' agregada exitosamente.{cerrarColor}")
    else:
        print(f"{rojoError}\nLa categoría '{nombre}' ya existe.{cerrarColor}")


# =============== SALIR DEL PROGRAMA =================
def salir():
    print("Gracias por jugar, no apuestes, juega por diversión")

    continuar = str(input("\nIngrese ENTER para salir".center(10, "-")))
    while(continuar != ""): 
        continuar = str(input(f"{rojoError}Error - Ingrese ENTER para salir{cerrarColor}".center(10, "-"))) 
    
    #Va a mostrar un print interactivo que va a gregando puntos cada 0.5s, simulando una animacion de salida del programa.
    print(f"{rojoError}Saliendo", end="", flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(f"{rojoError}.{cerrarColor}", end="", flush=True)

# ================= CARTEL BIENVENIDA =================
def cartel():
    
    winsound.PlaySound("sonidos/musica.wav", winsound.SND_ASYNC)
    
    cartel = """
    ╔════════════════════════════════════════════╗
    ║              🎰 CASINO ROYAL 🎰            ║
    ║ JUEGOS DE APUESTAS PROHIBIDOS PARA MENORES ║
    ║   Y PUEDEN SER PERJUDICIALES PARA LA SALUD ║
    ║            SOLO MAYORES DE 18 AÑOS         ║
    ╚════════════════════════════════════════════╝
        """
    
    for i in range(30):
        if i % 5 == 0:
            color = rojoNormal 
        elif i % 5 == 1:
            color = verde  
        elif i % 5 == 2:
            color = amarillo 
        elif i % 5 == 3:
            color = violeta
        else:
            color = azul  
        #Cambia el cartel cada 0.2s mientas se ejecuta el for, asi creamos un cartel interactivo que cambia de color.
        print("\033[H", end="")
        print(color + cartel + cerrarColor)
        time.sleep(0.2)
        
    winsound.PlaySound(None, winsound.SND_ASYNC)

          
    
    continuar = str(input("Ingrese ENTER para entrar".center(50, "-")))
    while(continuar != ""): 
        continuar = str(input(f"{rojoError}Error - Ingrese ENTER para entrar{cerrarColor}".center(50, "-"))) 

# ================ INICIO DEL PROGRAMA =================                         
inicio()
color()
cartel()
menu()


arcFisJug = "jugadores.dat"
arcFisCat = "categorias.dat"
arcFisOpc = "opcion.dat"

arcLogJug = abrirArchivo(arcFisJug)
arcLogCat = abrirArchivo(arcFisCat)
arcLogOpc = abrirArchivo(arcFisOpc)