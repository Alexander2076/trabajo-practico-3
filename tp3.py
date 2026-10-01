
import os, pickle, random as aleatorio, time, winsound, getpass

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
    global verde, rojoError, rosa, cerrarColor, amarillo, violeta, purpura, azul, rojoNormal, rojoIntenso, blanco, negro, cian
    rojoError = "\033[41m"
    rojoNormal = "\033[31m"
    rojoIntenso = "\033[1;38;5;196m"
    verde = "\033[1;32m"
    amarillo = "\033[1;33m"
    violeta = "\033[1;38;5;93m"
    rosa = "\033[1;38;5;200m"
    azul = "\033[1;34m"
    cian = "\033[1;36m"
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

def cerrarEnter():
    continuar = str(input("\nIngrese ENTER para continuar".center(10, "-")))
    while(continuar != ""): 
        continuar = str(input(f"{rojoError}Error - Ingrese ENTER para continuar{cerrarColor}".center(10, "-")))

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

def buscarNombre(nombre):
    global arcLogJug, arcFisJug

    index = 0
    tam = os.path.getsize(arcFisJug)
    arcLogJug.seek(0,0)

    if tam > 0:
        registro = pickle.load(arcLogJug)
        while arcLogJug.tell() < tam and registro.nombre != nombre:
            index = arcLogJug.tell()
            registro = pickle.load(arcLogJug)
        if registro.nombre == nombre:
            return index
        else:
            return -1
    else:
        return -1
    
def jugadorActual(pos): 
    global arcLogJug

    arcLogJug.seek(pos, 0)
    registro = pickle.load(arcLogJug)
    jugador = registro.nombre

    return jugador

def altaJugador(nombre):
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
    print(f"{cian}F. Administracion de juegos.{cerrarColor}")
    print(f"{rojoIntenso}S. Fin del PROGRAMA{cerrarColor}")
    
    print(f"{azul}{'═'*36}{cerrarColor}")

def menu(): 
    
    borrarPantalla()
    opc = ""
    while (opc != "s"):
        menuop()

        opc = str(input("\nIngrese la letra del menu: ")).lower()
        while (opc<"a" or opc>"f" and opc!="s"):
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
                menuReporte()
            case "f":
                winsound.PlaySound(None, winsound.SND_ASYNC)
                validarClave()
            case "s":
                salir()

# ================ REPORTE ================
def pantallaReporte():

    borrarPantalla()

    winsound.PlaySound("sonidos/juegos.wav", winsound.SND_ASYNC)

    print(f"{verde}╔════════════════════════════════════╗")
    print(f"{verde}║            📊 REPORTE 📊           ║")
    print(f"{verde}╚════════════════════════════════════╝{cerrarColor}")

    print(f"{amarillo}A - Lista de Jugadores {cerrarColor}")
    print(f"{cian}B - Juegos jugados por jugador{cerrarColor}")
    print(f"{azul}C - Volver al menú principal{cerrarColor}")

    print(f"{amarillo}{'═'*36}{cerrarColor}")

def menuReporte():

    borrarPantalla()

    opc = ""

    while (opc != "s"):
        pantallaReporte()

        opc = str(input("Ingrese la letra del menu: ")).lower()
        while (opc<"a" or opc>"c"):
            opc = str(input(f"{rojoError}Ingreso invalido - reintente{cerrarColor}"))

        match opc:
            case "a":
                borrarPantalla()
                listaJugadores()
            case "b":
                borrarPantalla()
                juegosJugados()
            case "c":
                borrarPantalla()
                menu()

def ordenarJugadoresPorCredito():
    global arcLogJug, arcFisJug

    arcLogJug.seek(0, 0)
    tam = os.path.getsize(arcFisJug)
    aux = pickle.load(arcLogJug)
    tamReg = arcLogJug.tell()
    cantReg = int(tam // tamReg)

    for i in range(0, cantReg - 1):
        for j in range(i + 1, cantReg):
            arcLogJug.seek(i * tamReg, 0)
            reg1 = pickle.load(arcLogJug)

            arcLogJug.seek(j * tamReg, 0)
            reg2 = pickle.load(arcLogJug)

            if int(reg1.credito) < int(reg2.credito):
                arcLogJug.seek(i * tamReg, 0)
                pickle.dump(reg2, arcLogJug)

                arcLogJug.seek(j * tamReg, 0)
                pickle.dump(reg1, arcLogJug)

def listaJugadores():
    global arcLogJug, arcFisJug

    arcLogJug.seek(0, 0)
    tam = os.path.getsize(arcFisJug)

    if tam > 0:
        ordenarJugadoresPorCredito()
        print(f"{amarillo}{'Nombre':<30}{'Credito':<10}{cerrarColor}")
        print(f"{amarillo}{'═'*40}{cerrarColor}")

        while arcLogJug.tell() < tam:
            regJugador = pickle.load(arcLogJug)
            print(f"{verde}{regJugador.nombre:<30}{regJugador.credito:<10}{cerrarColor}")

        cerrarEnter()
    else:
        print(f"{rojoError}\nNo hay jugadores registrados.{cerrarColor}")
        cerrarEnter()

def juegosJugados():
    global arcLogJug, arcFisJug

    arcLogJug.seek(0, 0)
    tam = os.path.getsize(arcFisJug)

    if tam > 0:
        nombre = validarNombre("Ingrese el nombre del jugador para consultar sus juegos: ").lower()
        pos = buscarNombre(nombre)
        if pos == -1:
            print(f"{rojoError}\nJugador no encontrado.{cerrarColor}")
            cerrarEnter()
        else:
            arcLogJug.seek(pos, 0)
            regJugador = pickle.load(arcLogJug)

            print(f"{cian}\nJuegos jugados por {regJugador.nombre.strip()}:{cerrarColor}")
            print(f"{cian}Credito actual: {regJugador.credito}{cerrarColor}\n")
            print(f"{amarillo}{'Partida':<30}{'Mayor o Menor':<15}{'Numero Secreto':<15}{'BlackJack':<15}{'Par o Impar':<15}{cerrarColor}")
            print(f"{amarillo}{'═'*90}{cerrarColor}")
            print(f"{verde}{'Ganados':<30}{regJugador.juegos[0][0]:<15}{regJugador.juegos[0][1]:<15}{regJugador.juegos[0][2]:<15}{regJugador.juegos[0][3]:<15}{cerrarColor}")
            print(f"{rojoNormal}{'Perdidos':<30}{regJugador.juegos[1][0]:<15}{regJugador.juegos[1][1]:<15}{regJugador.juegos[1][2]:<15}{regJugador.juegos[1][3]:<15}{cerrarColor}")
            cerrarEnter()
    else:
        print(f"{rojoError}\nNo hay jugadores registrados.{cerrarColor}")
        cerrarEnter()

# =============== ADMINISTRACION DE JUEGO =================
def validarClave():
    borrarPantalla()

    intentos = 3
    clave = getpass.getpass("\nIngrese la clave de administrador: ", echo_char="*")
    while (clave != CLAVE and intentos > 1):
        clave = getpass.getpass(f"{rojoError}\nClave incorrecta - reintente: {cerrarColor}", echo_char="*")
        intentos -= 1
    if intentos == 1 and clave != CLAVE:
        print(f"{rojoError}\nHa excedido el número de intentos permitidos, vuelva a intentarlo.{cerrarColor}")
        mensajeAnimado("Volviendo al menu", rojoError)
        time.sleep(1)

    else:
        admin()

def pantallaAdmin():
    borrarPantalla()
    print(f"{cian}╔════════════════════════════════════╗")
    print(f"{cian}║        ⚙️ ADMINISTRACION ⚙️          ║")
    print(f"{cian}╚════════════════════════════════════╝{cerrarColor}")

    print(f"{verde}A. Administrar Categorias.{cerrarColor}")
    print(f"{verde}B. Administrar Opciones.{cerrarColor}")
    print(f"{azul}C. Volver al menu principal.{cerrarColor}")

    print(f"{cian}{'═'*36}{cerrarColor}")

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


def pantallaAdminCategorias():
    borrarPantalla()
    print(f"{cian}╔════════════════════════════════════╗")
    print(f"{cian}║        ⚙️ ADMINISTRACION ⚙️          ║")
    print(f"{cian}╚════════════════════════════════════╝{cerrarColor}")

    print(f"{verde}a. Alta.{cerrarColor}")
    print(f"{verde}b. Modificacion.{cerrarColor}")
    print(f"{verde}c. Baja.{cerrarColor}")
    print(f"{azul}d. Volver al menu anterior.{cerrarColor}")

    print(f"{cian}{'═'*36}{cerrarColor}")

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
    print(f"{cian}╔════════════════════════════════════╗")
    print(f"{cian}║        ⚙️ ADMINISTRACION ⚙️          ║")
    print(f"{cian}╚════════════════════════════════════╝{cerrarColor}")

    print(f"{verde}a. Alta.{cerrarColor}")
    print(f"{verde}b. Consulta.{cerrarColor}")
    print(f"{azul}d. Volver al menu anterior.{cerrarColor}")

    print(f"{cian}{'═'*36}{cerrarColor}")

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
                altaOpciones()
            case "b":
                borrarPantalla()
                consultaOpciones()
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

def buscarNombreCategoria(nombre):
    global arcLogCat, arcFisCat

    index = 0
    tam = os.path.getsize(arcFisCat)
    arcLogCat.seek(0,0)

    if tam > 0:
        registro = pickle.load(arcLogCat)
        while arcLogCat.tell() < tam and registro.nombreCategoria != nombre:
            index = arcLogCat.tell()
            registro = pickle.load(arcLogCat)
        if registro.nombreCategoria == nombre:
            return index
        else:
            return -1
    else:
        return -1

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

    nombre = validarNombre("Ingrese el nombre de la categoría: ").lower()
    
    pos = buscarNombreCategoria(nombre)

    if pos == -1:
        regCategoria = categoria()
        arcLogCat.seek(0, 2)
        regCategoria.nroCategoria = regCategoria.nroCategoria + 1
        regCategoria.nombreCategoria = nombre
        pregunta = validarPregunta(nombre)
        regCategoria.pregunta = pregunta
        formatoCategoria(regCategoria)
        pickle.dump(regCategoria, arcLogCat)
        arcLogCat.flush()

        print(f"{verde}\nCategoría '{nombre}' agregada exitosamente.{cerrarColor}")
        cerrarEnter()
    else:
        print(f"{rojoError}\nLa categoría '{nombre}' ya existe.{cerrarColor}")
        cerrarEnter()

def listaCategoriasActivas():
    global arcLogCat, arcFisCat

    arcLogCat.seek(0, 0)
    tam = os.path.getsize(arcFisCat)

    if tam > 0:
        
        print(f"{azul}{'Activa':<5}{'Nro':<5}{'Nombre':<30}{cerrarColor}")
        print(f"{azul}{'═'*40}{cerrarColor}")

        while arcLogCat.tell() < tam:
            regCategoria = pickle.load(arcLogCat)
            if regCategoria.estado == "A":
                print(f"{verde}{regCategoria.estado:<5}{regCategoria.nroCategoria:<5}{regCategoria.nombreCategoria:<30}{cerrarColor}")

        return True
    else:
        print(f"{rojoError}\nNo hay categorías registradas.{cerrarColor}")
        cerrarEnter()
        return False

def buscarCategoriaNumero(nroCategoria):
    global arcLogCat, arcFisCat

    index = 0
    tam = os.path.getsize(arcFisCat)
    arcLogCat.seek(0,0)
    registro = pickle.load(arcLogCat)

    while arcLogCat.tell() < tam and int(registro.nroCategoria) != nroCategoria and registro.estado == "A":
        index = arcLogCat.tell()
        registro = pickle.load(arcLogCat)
    if int(registro.nroCategoria) == nroCategoria and registro.estado == "A":
        return index
    else:
        return -1
    

def modificarCategoria():
    borrarPantalla()
    print(f"{amarillo}╔════════════════════════════════════╗")
    print(f"{amarillo}║      ⚙️ MODIFICAR CATEGORIA ⚙️     ║")
    print(f"{amarillo}╚════════════════════════════════════╝{cerrarColor}")

    global arcLogCat, arcFisCat

    validar = listaCategoriasActivas()

    if validar:
        numero = int(input(f"\nIngrese el número de la categoría a modificar: "))
        pos = buscarCategoriaNumero(numero)
        while pos == -1:
            numero = int(input(f"{rojoError}\nError - Ingrese un número válido de categoría: {cerrarColor}"))
            pos = buscarCategoriaNumero(numero)
   
        if pos != -1:
            arcLogCat.seek(pos, 0)
            regCategoria = pickle.load(arcLogCat)
            nombre = regCategoria.nombreCategoria.strip()
            nuevo_nombre = validarNombre("Ingrese el nuevo nombre de la categoría: ").lower()

            regCategoria.nombreCategoria = nuevo_nombre
            formatoCategoria(regCategoria)

            arcLogCat.seek(pos, 0)
            pickle.dump(regCategoria, arcLogCat)
            arcLogCat.flush()

            print(f"{verde}\nCategoría '{nombre}' modificada exitosamente.{cerrarColor}")
            cerrarEnter()
        else:
            print(f"{rojoError}\nLa categoría '{nombre}' no existe.{cerrarColor}")
            cerrarEnter()

def bajaCategoria():
    borrarPantalla()
    print(f"{rojoError}╔════════════════════════════════════╗")
    print(f"{rojoError}║        ⚙️ BAJA CATEGORIA ⚙️          ║")
    print(f"{rojoError}╚════════════════════════════════════╝{cerrarColor}")

    global arcLogCat, arcFisCat

    validar = listaCategoriasActivas()

    if validar:
        numero = int(input(f"\nIngrese el número de la categoría a dar de baja: "))
        pos = buscarCategoriaNumero(numero)
        while pos == -1:
            numero = int(input(f"{rojoError}\nError - Ingrese un número válido de categoría: {cerrarColor}"))
            pos = buscarCategoriaNumero(numero)

        if pos != -1:
            arcLogCat.seek(pos, 0)
            regCategoria = pickle.load(arcLogCat)
            nombre = regCategoria.nombreCategoria.strip()

            regCategoria.estado = "I"
            formatoCategoria(regCategoria)

            arcLogCat.seek(pos, 0)
            pickle.dump(regCategoria, arcLogCat)
            arcLogCat.flush()

            print(f"{verde}\nCategoría '{nombre}' dada de baja exitosamente.{cerrarColor}")
            cerrarEnter()
        else:
            print(f"{rojoError}\nLa categoría '{nombre}' no existe.{cerrarColor}")
            cerrarEnter()

# =============== ADMINISTRACION DE OPCIONES =================
def formatoOpcion(regOpcion):
    regOpcion.nroCategoria = str(regOpcion.nroCategoria).ljust(3, " ")
    regOpcion.nroOpcion = str(regOpcion.nroOpcion).ljust(3, " ")
    regOpcion.objeto = regOpcion.objeto.ljust(100, " ")
    regOpcion.valor = str(regOpcion.valor).ljust(12, " ")

def altaOpciones():
    borrarPantalla()
    print(f"{verde}╔════════════════════════════════════╗")
    print(f"{verde}║        ⚙️ ALTA OPCIONES ⚙️         ║")
    print(f"{verde}╚════════════════════════════════════╝{cerrarColor}")

    global arcLogOpc, arcFisOpc

    validar = listaCategoriasActivas()

    if validar:
        nroCategoria = int(input(f"\nIngrese el número de la categoría para agregar opciones: "))
        pos = buscarCategoriaNumero(nroCategoria)
        while pos == -1:
            nroCategoria = int(input(f"{rojoError}\nError - Ingrese un número válido de categoría: {cerrarColor}"))
            pos = buscarCategoriaNumero(nroCategoria)

        if pos != -1:
            arcLogOpc.seek(0, 2)
            regOpcion = opcion()
            regOpcion.nroCategoria = nroCategoria
            regOpcion.nroOpcion = regOpcion.nroOpcion + 1
            regOpcion.objeto = str(input(f"\nIngrese la opción para la categoría '{nroCategoria}': ")).strip()
            regOpcion.valor = int(input(f"\nIngrese el valor de la opción '{regOpcion.objeto}': "))
            formatoOpcion(regOpcion)
            pickle.dump(regOpcion, arcLogOpc)
            arcLogOpc.flush()

            print(f"{verde}\nOpción '{regOpcion.objeto}' agregada exitosamente a la categoría '{nroCategoria}'.{cerrarColor}")
            cerrarEnter()
        else:
            print(f"{rojoError}\nLa categoría '{nroCategoria}' no existe.{cerrarColor}")
            cerrarEnter()

def consultaOpciones():
    borrarPantalla()
    print(f"{azul}╔════════════════════════════════════╗")
    print(f"{azul}║       ⚙️ CONSULTA OPCIONES ⚙️      ║")
    print(f"{azul}╚════════════════════════════════════╝{cerrarColor}")

    global arcLogOpc, arcFisOpc

    validar = listaCategoriasActivas()

    if validar:
        nroCategoria = int(input(f"\nIngrese el número de la categoría para consultar opciones: "))
        pos = buscarCategoriaNumero(nroCategoria)
        while pos == -1:
            nroCategoria = int(input(f"{rojoError}\nError - Ingrese un número válido de categoría: {cerrarColor}"))
            pos = buscarCategoriaNumero(nroCategoria)

        if pos != -1:
            arcLogOpc.seek(0, 0)
            tam = os.path.getsize(arcFisOpc)

            print(f"{amarillo}{'Nro Cat':<10}{'Nro Op':<10}{'Opción':<100}{'Valor':<12}{cerrarColor}")
            print(f"{amarillo}{'═'*132}{cerrarColor}")

            while arcLogOpc.tell() < tam:
                regOpcion = pickle.load(arcLogOpc)
                if int(regOpcion.nroCategoria) == nroCategoria:
                    print(f"{verde}{regOpcion.nroCategoria:<10}{regOpcion.nroOpcion:<10}{regOpcion.objeto:<100}{regOpcion.valor:<12}{cerrarColor}")
            cerrarEnter()
        else:
            print(f"{rojoError}\nLa categoría '{nroCategoria}' no existe.{cerrarColor}")
            cerrarEnter()

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
CLAVE = "1234"

arcFisJug = "jugadores.dat"
arcFisCat = "categorias.dat"
arcFisOpc = "opcion.dat"

arcLogJug = abrirArchivo(arcFisJug)
arcLogCat = abrirArchivo(arcFisCat)
arcLogOpc = abrirArchivo(arcFisOpc)

#inicio()
color()
cartel()
menu()
