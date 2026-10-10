import pickle, os, random as aleatorio, time, getpass



def color():
    global verde, rojoError, rosa, cerrarColor, fondoVerde, amarillo, violeta, purpura, azul, rojoNormal, rojoIntenso, blanco, negro
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
    fondoVerde = "\033[42m"
    cerrarColor = "\033[0m"

def array(tipo, tam): 
    array = [tipo] * tam
    return array

def matriz(filas, columnas, tipo):
    matriz = [tipo] * filas

    for i in range(filas):
        matriz[i] = [tipo] * columnas
    
    return matriz


class categorias: 
    def __init__(self):
        self.NroCategoria = 0
        self.NombreCategoria = ""
        self.Pregunta = ""
        self.Estado = ""
        self.Tipo = 0

class opciones: 
    def __init__(self):
        self.NroCategoria = 0
        self.NroOpcion = 0
        self.objeto = ""
        self.valor = 0

class jugadores:
    def __init__(self):
        self.Nombre = ""
        self.Creditos = 0.0
        self.Juegos = matriz(4, 3, 0)


def continuar():
    enter = str(input(f"{blanco}--- Presiona ENTER para continuar ---{cerrarColor}"))
    while enter != "":
       enter = str(input(f"{blanco}--- Presiona ENTER para continuar ---{cerrarColor}"))


def validarCodigo(): 
    entrada = input("ingrese un numero de categoria o (0) para salir: ")
    numeroC = -1
    while numeroC == -1:
        try:
            numeroC = int(entrada)
        except ValueError:
            print(f"{rojoIntenso}Solo puedes ingresar numeros!{cerrarColor}")
            entrada = input("ingrese un numero de categoria o (0) para salir: ")
    return numeroC
        

def formatearJug(rJugador):
    rJugador.Nombre = rJugador.Nombre.ljust(30, " ")
    rJugador.Creditos = str(rJugador.Creditos)
    rJugador.Creditos = rJugador.Creditos.ljust(7, " ")
    for i in range(4): 
        for j in range(2): 
            rJugador.Juegos[i][j] = str(rJugador.Juegos[i][j])
            rJugador.Juegos[i][j] = rJugador.Juegos[i][j].ljust(2, " ")
   
   
    
def desformatearJug(rJugador):

    rJugador.Nombre = rJugador.Nombre.strip()

    rJugador.Creditos = float(rJugador.Creditos.strip())

    for i in range(4):
        for j in range(2):
            rJugador.Juegos[i][j] = int(rJugador.Juegos[i][j].strip())
  
            
def formatearCat(categoria): 
    categoria.NroCategoria = str(categoria.NroCategoria).ljust(2, " ")
    categoria.NombreCategoria = categoria.NombreCategoria.ljust(30, " ")
    categoria.Pregunta = categoria.Pregunta.ljust(200, " ")

def desformatearCat(categoria):
    categoria.NroCategoria = int(categoria.NroCategoria.strip())
    categoria.NombreCategoria = categoria.NombreCategoria.strip()
    categoria.Pregunta = categoria.Pregunta.strip()

def formatearOpc(opcion):

    opcion.NroCategoria = str(opcion.NroCategoria).ljust(2, " ")
    opcion.NroOpcion = str(opcion.NroOpcion).ljust(2, " ")
    opcion.objeto = opcion.objeto.ljust(100, " ")
    opcion.valor = str(opcion.valor).ljust(6, " ")
def desformatearOpc(opcion):

    opcion.NroCategoria = int(opcion.NroCategoria.strip())
    opcion.NroOpcion = int(opcion.NroOpcion.strip())
    opcion.objeto = opcion.objeto.strip()
    opcion.valor = int(opcion.valor.strip())

    
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

def mensajeAnimado(mensaje, color):

    print(f"{color}{mensaje}", end="", flush=True)
    for i in range(3):
        time.sleep(0.4)
        print(f"{color}.{cerrarColor}", end="", flush=True)

def guardar(jugador, posicion): 
    global archivoLogJug
    formatearJug(jugador)
    archivoLogJug.seek(posicion, 0)
    pickle.dump(jugador, archivoLogJug)
    archivoLogJug.flush()
    # mensajeAnimado("\nguardando datos", azul)

def animacion(jugador, mensaje, resultado):

    texto = f"{jugador} {mensaje}".center(50)
    # if(resultado == "gano"): 
    #             winsound.PlaySound("sonidos/ganaste.wav", winsound.SND_ASYNC)
    # else: 
    #             winsound.PlaySound("sonidos/perdiste.wav", winsound.SND_ASYNC)
            

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
                color = fondoVerde

        elif resultado == "perdio":

            if i % 5 == 0:
                color = rojoNormal
            elif i % 5 == 1:
                color = rojoIntenso
            elif i % 5 == 2:
                color = rojoIntenso
            elif i % 5 == 3:
                color = rojoNormal
            else:
                color = rojoError
        print(f"\r{color}{texto}{cerrarColor}", end="")
        time.sleep(0.1)

    print()
    
def buscarJugador(nombre): 
    global archivoFisJug, archivoLogJug
    t = os.path.getsize(archivoFisJug)
    pos=0
    archivoLogJug.seek(0, 0)  
    if t>0:
        jugador = pickle.load(archivoLogJug)
        desformatearJug(jugador)
        while (archivoLogJug.tell()<t) and (jugador.Nombre != nombre):
            pos = archivoLogJug.tell()
            jugador = pickle.load(archivoLogJug)
            desformatearJug(jugador)
        if jugador.Nombre == nombre:        
            return pos
        else:
             return -1
    else:
            return -1

    
def crearJugador(nombre):
    global archivoLogJug
    nuevoJugador = jugadores()
    nuevoJugador.Nombre = nombre
    nuevoJugador.Creditos = 10000
    
    formatearJug(nuevoJugador)
    archivoLogJug.seek(0, 2)
    posicion = archivoLogJug.tell()
    pickle.dump(nuevoJugador, archivoLogJug)  
  
    archivoLogJug.flush()
    return posicion

def iniciarJuego(): 

    
    print(f"{amarillo}╔══════════════════════════════════════╗{cerrarColor}")
    print(f"{amarillo}║          INGRESAR NOMBRE          {amarillo}   ║{cerrarColor}")
    print(f"{amarillo}╚══════════════════════════════════════╝{cerrarColor}")

    nombre = input(f"{amarillo}  ➜  {cerrarColor}")
    posicion = buscarJugador(nombre)
    if (posicion == -1): 
        posicion = crearJugador(nombre)
    return posicion
         




def busCategoria(nombreC): 
    global archivoFisCat, archivoLogCat
    t = os.path.getsize(archivoFisCat)
   
    archivoLogCat.seek(0, 0)  
    if t>0:
            categoria = pickle.load(archivoLogCat)
            desformatearCat(categoria)
            while (archivoLogCat.tell()<t) and categoria.NombreCategoria != nombreC:
                categoria = pickle.load(archivoLogCat)
                desformatearCat(categoria)
            if categoria.NombreCategoria == nombreC:        
                return 1
            else:
                 return -1
    else:
                return -1
def busCategoriaDic(numeroC): 
    global archivoFisCat, archivoLogCat
    archivoLogCat.seek(0, 0)
    aux = pickle.load(archivoLogCat)
    tamCat = archivoLogCat.tell()
    t = os.path.getsize(archivoFisCat)
    cantidadC = t // tamCat
    inferior = 0
    superior = cantidadC-1
    medio = (inferior + superior) // 2 					
    archivoLogCat.seek(medio*tamCat, 0)
    categoria = pickle.load(archivoLogCat) 	
    desformatearCat(categoria)				
    while categoria.NroCategoria != int(numeroC) and (inferior < superior):
                if int(numeroC) < categoria.NroCategoria:
                    superior = medio - 1
                else:
                    inferior = medio + 1
                medio = (inferior + superior) // 2 
                archivoLogCat.seek(medio*tamCat, 0)
                categoria = pickle.load(archivoLogCat)
                desformatearCat(categoria)
    if categoria.NroCategoria == int(numeroC):						
                return medio*tamCat							
    else:
        return -1
    


    
   
def crearCategoria(nombreCat): 
    global archivoLogCat, archivoFisCat
    archivoLogCat.seek(0, 0)
    t = os.path.getsize(archivoFisCat) 
    if(t == 0): 
        nroCat = 0
    else: 
        categoria = pickle.load(archivoLogCat)
        tamCat = archivoLogCat.tell()
        nroCat = t // tamCat
    nuevaCategoria = categorias()
    nuevaCategoria.NroCategoria = nroCat + 1 
    nuevaCategoria.NombreCategoria = nombreCat
    nuevaCategoria.Estado = "A"
    preguntaCategoria = str(input(f"{azul}ingrese una pregunta para la categoria: {cerrarColor}"))
    tipoCategoria = int(input("ingrese el tipo de categoria 1.mayor 2.menor"))
    nuevaCategoria.Pregunta = preguntaCategoria
    nuevaCategoria.Tipo = tipoCategoria
    formatearCat(nuevaCategoria)
    archivoLogCat.seek(0, 2)
    pickle.dump(nuevaCategoria, archivoLogCat)
    archivoLogCat.flush()
    print(f"{verde}categoria creada correctamente!{cerrarColor}")
    

def altaCategoria():
    print(f"{amarillo} DAR DE ALTA A CATEGORIAS {cerrarColor}")
    nombreCat = str(input("ingrese el nombre de la categoria o (*) para salir: "))
    while  (nombreCat != "*"): 
        resultado = busCategoria(nombreCat)
        if(resultado == -1): 
            crearCategoria(nombreCat)
        else: 
            print(f"{rojoIntenso}esa categoria ya existe! ingresa otro nombre!{cerrarColor}")
        nombreCat = str(input("ingrese el nombre de la categoria o (*) para salir: "))


def limpiarPantalla(): 
    print("\033[H\033[J", end="")
    
def listarCategorias():
    global archivoLogCat, archivoFisCat

    t = os.path.getsize(archivoFisCat)

    archivoLogCat.seek(0, 0)

    print("\033[1;36m══════════════════════════════════════════════\033[0m")
    print("              \033[1;93mCATEGORÍAS\033[0m")
    print("\033[1;36m──────────────────────────────────────────────\033[0m")
    print("  \033[1;93mCódigo\033[0m                              \033[1;93mNombre\033[0m")
    print("\033[1;36m──────────────────────────────────────────────\033[0m")

    while archivoLogCat.tell() < t:

        categoria = pickle.load(archivoLogCat)

        if categoria.Estado.strip() == "A":
            color = "\033[1;92m"   # Verde
        else:
            color = "\033[1;91m"   # Rojo

        print(f"  {color}[{categoria.NroCategoria.strip()}]"
              f"{categoria.NombreCategoria.strip():>39}\033[0m")

    print("\033[1;36m══════════════════════════════════════════════\033[0m")
 



def modificarCategoria(): 
    global archivoFisCat, archivoLogCat
    print(f"{amarillo} MODIFICAR CATEGORIAS {cerrarColor}")
    t = os.path.getsize(archivoFisCat)

    if(t == 0): 
        print(f"{rojoNormal}no hay categorias cargadas...{cerrarColor}")
        continuar()
    else: 
        listarCategorias()

        numeroC = validarCodigo()

        while numeroC != 0: 
            
            posicion = busCategoriaDic(numeroC)

            if(posicion != -1): 

                archivoLogCat.seek(posicion, 0)
                categoria = pickle.load(archivoLogCat)
                desformatearCat(categoria)
                if categoria.Estado == "A":

                    nuevoNombre = str(input(f"{azul}ingresa el nuevo nombre para la categoria: {cerrarColor}"))
                    confirmar = str(input("estas seguro que desea modificar la categoria? S / N: ")).upper()

                    while confirmar != "N" and confirmar != "S":
                        confirmar = str(input("estas seguro que desea modificar la categoria? S / N: ")).upper()

                    if(confirmar == "S"):
                        categoria.NombreCategoria = nuevoNombre
                        formatearCat(categoria)
                        archivoLogCat.seek(posicion, 0)
                        pickle.dump(categoria, archivoLogCat)
                        archivoLogCat.flush()

                        print(f"{verde}categoria modificada correctamente!{cerrarColor}")
                        time.sleep(2)

                    else: 
                        print(f"{rojoIntenso}cancelado{cerrarColor}")
                        time.sleep(2)

                else:
                    print(f"{rojoIntenso}solo puedes modificar categorias activas!{cerrarColor}")
                    time.sleep(2)

            else: 
                print(f"{rojoIntenso}ingrese un numero de categoria valido!{cerrarColor}")
                time.sleep(2)
            limpiarPantalla()
            print(f"{amarillo} MODIFICAR CATEGORIAS {cerrarColor}")
            listarCategorias()
            numeroC = validarCodigo()
    

def bajaCategoria(): 
    global archivoLogCat, archivoFisCat
    print(f"{amarillo}BAJAS DE CATEGORIAS{cerrarColor}")
    t = os.path.getsize(archivoFisCat)

    if(t == 0): 
        print(f"{rojoNormal}no hay categorias cargadas...{cerrarColor}")
        continuar()
    else: 
        listarCategorias()

        numeroC = validarCodigo()

        while numeroC != 0: 
            
            posicion = busCategoriaDic(numeroC)

            if(posicion != -1): 

                archivoLogCat.seek(posicion, 0)
                categoria = pickle.load(archivoLogCat)

                if categoria.Estado.strip() == "A":

                    confirmar = str(input("estas seguro que desea dar de baja a la categoria? S / N: ")).upper()

                    while confirmar != "N" and confirmar != "S":
                        confirmar = str(input("estas seguro que desea dar de baja a la categoria? S / N: ")).upper()

                    if(confirmar == "S"):

                        categoria.Estado = "I"

                        archivoLogCat.seek(posicion, 0)

                        formatearCat(categoria)

                        pickle.dump(categoria, archivoLogCat)
                        archivoLogCat.flush()

                        print(f"{verde}categoria dada de baja correctamente!{cerrarColor}")
                        continuar()

                    else: 
                        print(f"{rojoIntenso}cancelado{cerrarColor}")
                        continuar()

                else:
                    print(f"{rojoIntenso}la categoria ya se encuentra dada de baja!{cerrarColor}")
                    continuar()

            else: 
                print(f"{rojoIntenso}ingrese un numero de categoria valido!{cerrarColor}")
                continuar()
            limpiarPantalla()
            print(f"{amarillo}BAJAS DE CATEGORIAS{cerrarColor}")
            listarCategorias()
            numeroC = validarCodigo()


def menuop():
    limpiarPantalla()
    
    print(f"{azul}MENU PRINCIPAL{cerrarColor}")
    print(f"{azul}{'═'*36}{cerrarColor}")
    print(f"{violeta}[A]. Juego del Menor-Mayor.{cerrarColor}")
    print(f"{rosa}[B]. Adivinar el Número Secreto.{cerrarColor}")
    print(f"{amarillo}[C]. Blackjack.{cerrarColor}")
    print(f"{azul}[D]. Par o Impar.{cerrarColor}")
    print(f"{verde}[E]. Reporte.{cerrarColor}")
    print(f"{violeta}[F]. Administración de Juegos.{cerrarColor}")
    print(f"{rojoIntenso}[G]. Salir del programa.{cerrarColor}")
    print(f"{azul}{'═'*36}{cerrarColor}")
    
    

def submenu1():

    limpiarPantalla()

    print(f"{amarillo}╔══════════════════════════════════════════╗{cerrarColor}")
    print(f"{amarillo}║          🎰 ADMINISTRACIÓN 🎰            ║{cerrarColor}")
    print(f"{amarillo}╠══════════════════════════════════════════╣{cerrarColor}")
    print(f"{verde}║  [1]  📁 Administrar Categorías          ║{cerrarColor}")
    print(f"{azul}║  [2]  🎲 Administrar Opciones            ║{cerrarColor}")
    print(f"{rojoNormal}║  [3]  ↩  Volver                          ║{cerrarColor}")
    print(f"{amarillo}╚══════════════════════════════════════════╝{cerrarColor}")
    
    
def submenu2():

    limpiarPantalla()

    print(f"{amarillo}╔══════════════════════════════════════════╗{cerrarColor}")
    print(f"{amarillo}║       📁 ADMINISTRAR CATEGORÍAS 📁       ║{cerrarColor}")
    print(f"{amarillo}╠══════════════════════════════════════════╣{cerrarColor}")
    print(f"{verde}║  [1]  ➕ Alta                            ║{cerrarColor}")
    print(f"{azul}║  [2]  ✏️  Modificación                    ║{cerrarColor}")
    print(f"{rojoNormal}║  [3]  🗑️  Baja                            ║{cerrarColor}")
    print(f"{amarillo}║  [4]  ↩  Volver                          ║{cerrarColor}")
    print(f"{amarillo}╚══════════════════════════════════════════╝{cerrarColor}")
    
    
def submenu3():

    limpiarPantalla()

    print(f"{amarillo}╔══════════════════════════════════════════╗{cerrarColor}")
    print(f"{amarillo}║        🎲 ADMINISTRAR OPCIONES 🎲        ║{cerrarColor}")
    print(f"{amarillo}╠══════════════════════════════════════════╣{cerrarColor}")
    print(f"{verde}║  [1]  ➕ Alta                            ║{cerrarColor}")
    print(f"{azul}║  [2]  🔍 Consulta                        ║{cerrarColor}")
    print(f"{rojoNormal}║  [3]  ↩  Volver                          ║{cerrarColor}")
    print(f"{amarillo}╚══════════════════════════════════════════╝{cerrarColor}")

    
def admCategorias(): 
   
    opcion3 = 0
    while opcion3 != 4: 
        submenu2()
        opcion3 = int(input("ingrese una opcion: "))
        if(opcion3 == 1): 
            limpiarPantalla()
            altaCategoria()
        elif(opcion3 == 2): 
            limpiarPantalla()
            modificarCategoria()
        elif(opcion3 == 3): 
            limpiarPantalla()
            bajaCategoria()
        elif(opcion3 == 4): 
            mensajeAnimado("saliendo", rojoError)
        else: 
            print(f"{rojoIntenso}ingrese una opcion valida...{cerrarColor}")

def contarOpciones(numeroC):
    global archivoLogOpc, archivoFisOpc

    t = os.path.getsize(archivoFisOpc)
    contador = 1

    archivoLogOpc.seek(0, 0)

    while archivoLogOpc.tell() < t:
        opcion = pickle.load(archivoLogOpc)
        desformatearOpc(opcion)
        if opcion.NroCategoria == numeroC:
            contador = contador + 1
           
    return contador   

def existeObjeto(numeroC, objeto):
  
    global archivoLogOpc, archivoFisOpc

    t = os.path.getsize(archivoFisOpc)

    archivoLogOpc.seek(0, 0)

    while archivoLogOpc.tell() < t:
        opcion = pickle.load(archivoLogOpc)
        desformatearOpc(opcion)
        if opcion.NroCategoria == numeroC:
            if opcion.objeto == objeto:
               
                return 1

    return -1

def cargarOpcion(numeroC, categoria, nroOpcion):
    global archivoLogOpc

    opcion = opciones()

    opcion.NroCategoria = categoria.NroCategoria
    opcion.NroOpcion = nroOpcion

    objeto = input("ingrese la opcion para la categoria: ")

    while existeObjeto(numeroC, objeto) == 1:
        print(f"{rojoError}esa opcion ya existe para esta categoria!{cerrarColor}")
        objeto = input("ingrese otra opcion: ")

    valor = int(input("ingrese el valor para la opcion: "))

    opcion.objeto = objeto
    opcion.valor = valor
    formatearOpc(opcion)
    archivoLogOpc.seek(0, 2)
    pickle.dump(opcion, archivoLogOpc)
    archivoLogOpc.flush()

    print(f"{verde}opcion cargada correctamente!!{cerrarColor}")


def altaOpcion():
    global archivoFisCat, archivoLogOpc, archivoLogCat
    limpiarPantalla()
    print(f"{amarillo}ALTA DE OPCIONES{cerrarColor}")
    t = os.path.getsize(archivoFisCat)

    if(t == 0): 
        print(f"{rojoNormal}aun no hay categorias cargadas...{cerrarColor}")
        continuar()
        
    else: 
        
        listarCategorias()

        numeroC = validarCodigo()

        while numeroC != 0: 
            
            pos = busCategoriaDic(numeroC)

            if(pos != -1): 

                archivoLogCat.seek(pos, 0)
                categoria = pickle.load(archivoLogCat)
                desformatearCat(categoria)
                if(categoria.Estado == "A"):

                    print(f"{azul}categoria: {categoria.NombreCategoria} {cerrarColor}")
                    print(f"{amarillo}Pregunta: ¿{categoria.Pregunta}? {cerrarColor}")

                    nroOpcion = contarOpciones(numeroC)

                    while nroOpcion <= 6:

                        cargarOpcion(numeroC, categoria, nroOpcion)

                        nroOpcion = nroOpcion + 1
                        
                    seguir = input("desea cargar otra opcion? S/N: ").upper()

                    while seguir == "S":

                        cargarOpcion(numeroC, categoria, nroOpcion)

                        nroOpcion = nroOpcion + 1

                        seguir = input("desea cargar otra opcion? S/N: ").upper()

                else:
                    print(f"{rojoIntenso}esa categoria se encuentra dada de baja.{cerrarColor}")
                    time.sleep(2)

            else: 
                print(f"{rojoIntenso}no existe ese numero de categoria!{cerrarColor}")
                time.sleep(2)
            limpiarPantalla()
            print(f"{amarillo}ALTA DE OPCIONES{cerrarColor}")
            listarCategorias()
            numeroC = validarCodigo()
    

def listaropciones(numeroC, regC): 
    
    global archivoFisOpc, archivoLogOpc 
    limpiarPantalla()
    print(f"{amarillo}OPCIONES DE LA CATEGORIA{cerrarColor}")
    t = os.path.getsize(archivoFisOpc) 

    archivoLogOpc.seek(0, 0)

    contador = 0
    
    print("\033[1;36m═════════════════════════════════════════════════════\033[0m") 
    print(f"  \033[1;97mCategoría:\033[0m {regC.NroCategoria}") 
    print(f"  \033[1;93m¿ {regC.Pregunta} ?") 
    print("\033[1;36m═════════════════════════════════════════════════════\033[0m") 
 
    while archivoLogOpc.tell() < t: 
 
        opcion = pickle.load(archivoLogOpc) 
        desformatearOpc(opcion)
        if opcion.NroCategoria == numeroC: 

            contador = contador + 1
 
            print(f"  \033[1;95m[{opcion.NroOpcion}]\033[0m "
                  f"\033[1;97m{opcion.objeto:<30}\033[0m"
                  f"\033[1;93m{opcion.valor:>10}\033[0m") 

    if contador == 0:
        print("  \033[1;91mNo hay opciones cargadas para esta categoría.\033[0m")
 
    print("\033[1;36m═════════════════════════════════════════════════════\033[0m")

    continuar()



                
def consultaCat(): 
    global archivoFisCat, archivoLogOpc, archivoLogCat
    limpiarPantalla()
    print(f"{amarillo}CONSULTA DE CATEGORIAS{cerrarColor}")
    t = os.path.getsize(archivoFisCat)
    
    if(t == 0): 
        print(f"{rojoNormal}no hay categorias cargadas...{cerrarColor}")
        continuar()
    else: 
        listarCategorias()
        numeroC = validarCodigo()
        while numeroC != 0: 
           
            pos = busCategoriaDic(numeroC)
          
            if(pos != -1): 
                archivoLogCat.seek(pos, 0)
                categoria = pickle.load(archivoLogCat)
                desformatearCat(categoria)
                if(categoria.Estado == "A"):
                  listaropciones(numeroC, categoria)
                else: 
                    print(f"{rojoIntenso}la categoria esta dada de baja! no te puedo mostrar las opciones.{cerrarColor}")
                    time.sleep(2)
            else: 
                print(f"{rojoIntenso}no existe esa categoria, ingresa otra!{cerrarColor}")
                time.sleep(2)
            limpiarPantalla()
            print(f"{amarillo}CONSULTA DE CATEGORIAS{cerrarColor}")
            listarCategorias()
            numeroC = validarCodigo()
            
        
        


def admOpciones(): 

    opcion4 = 0
    while opcion4 != 3: 
        submenu3()
        opcion4 = int(input("ingrese una opcion: "))
        if(opcion4 == 1): 
            limpiarPantalla()
            altaOpcion()
        elif(opcion4 == 2): 
            limpiarPantalla()
            consultaCat()
        elif(opcion4 == 3): 
            mensajeAnimado("Saliendo", rojoError)
        else: 
            print("ingrese una opcion valida...")

def administracion(): 
    print("administraciòn")
    opcion2 = 0
    while opcion2 != 3: 
        submenu1()
        opcion2 = int(input("ingrese una opcion: "))
        if(opcion2 == 1): 
            admCategorias()
        elif(opcion2 == 2): 
            admOpciones()
        elif (opcion2 == 3): 
            mensajeAnimado("saliendo", rojoError)
        else: 
            print("ingrese una opcion valida! ")
            
            
def verificar(c):
    
    
    intentos = 0
    correcto = "no"
    while intentos < 3 and correcto == "no":
        limpiarPantalla()
        print(f"{amarillo}ADMINISTRACION (ACCESO RESTRINGIDO){cerrarColor}")
        print(f"{verde}╔══════════════════════════════════════╗{cerrarColor}")
        print(f"{verde}║          INGRESAR CONTRASEÑA         ║{cerrarColor}")
        print(f"{verde}╚══════════════════════════════════════╝{cerrarColor}")
        contIngresada = getpass.getpass(f"{verde} ➜ ", echo_char="*")
        print(cerrarColor)
        if(contIngresada != c): 
            intentos += 1
            if(intentos < 3): 
             print(f"{rojoIntenso}✖ contraseña incorrecta, ingresa nuevamente! tienes {3 - intentos} intentos.{cerrarColor}")
             print(f"{amarillo}Tienes {3 - intentos} intentos{cerrarColor}")
             time.sleep(2)
             
        else: 
            correcto = "si"
    if(correcto == "si"):
        mensajeAnimado("accediendo", verde)
        administracion()
    else: 
        print(f"{rojoIntenso}Superó los 3 intentos de ingresar contraseña, salga e intente nuevamente!{cerrarColor}")
        time.sleep(3)
        
def obtenerOpciones(numeroC, arrOp): 
    global archivoLogOpc, archivoFisOpc

    t = os.path.getsize(archivoFisOpc)
    
    i = 0
    cantidad = 0
    archivoLogOpc.seek(0, 0)

    while archivoLogOpc.tell() < t:
        opcion = pickle.load(archivoLogOpc)
        desformatearOpc(opcion)
        
        if opcion.NroCategoria == numeroC:

            cantidad += 1

            if cantidad <= 6:
                arrOp[i] = opcion
                i += 1
            else:
                posicion = aleatorio.randint(0, 5)
                arrOp[posicion] = opcion      
    return i
        
    
           
     

def elegirCategoria(op): 
    global archivoLogCat, archivoFisCat
    t = os.path.getsize(archivoFisCat)
    archivoLogCat.seek(0, 0)

    contador = 1

    while archivoLogCat.tell() < t:

        categoria = pickle.load(archivoLogCat)
        desformatearCat(categoria)
        if categoria.Estado == "A":

            if contador == op:
                return categoria.NroCategoria

            contador = contador + 1
    
    
    
def menuCategorias():
    
    global archivoFisCat, archivoLogCat

    t = os.path.getsize(archivoFisCat)
    if(t == 0): 
        limpiarPantalla()
        print(f"{rojoIntenso}aun no hay categorias cargadas!{cerrarColor}")
        return -1
    else: 
        
        archivoLogCat.seek(0, 0)
        contador = 1

        print()
        print(f"{azul}{'=' * 45}{cerrarColor}")
        print(f"{amarillo}        MAYOR O MENOR - CATEGORÍAS{cerrarColor}")
        print(f"{azul}{'=' * 45}{cerrarColor}")
        print()

        print(f"{rosa}Seleccione una categoría:{cerrarColor}")
        print()

        while archivoLogCat.tell() < t: 
            categoria = pickle.load(archivoLogCat)
            desformatearCat(categoria)

            if(categoria.Estado == "A"):
                print(f"{verde}  [{contador}] {cerrarColor}{categoria.NombreCategoria}")
                contador = contador + 1
        if contador == 1:
            
            limpiarPantalla()
            print(f"{rojoIntenso}No hay categorías activas para jugar.{cerrarColor}")
            
            return -1
        print()
        print(f"{azul}{'-' * 45}{cerrarColor}")

        opcion = int(input(f"{rosa}Seleccione una categoría: {cerrarColor}"))

        while opcion < 1 or opcion >= contador:
            print()
            print(f"{rojoError}Opción inválida. Seleccione nuevamente.{cerrarColor}")
            opcion = int(input(f"{rosa}Seleccione una categoría: {cerrarColor}"))
        resultado = elegirCategoria(opcion)
        return resultado


    
def validarCredito(creditoAc): 
    credito = float(input(f"{amarillo}Cuanto credito quieres apostar? tu credito actual es de ${creditoAc}: {cerrarColor}"))
    while(credito < 1 or credito > creditoAc): 
         credito = float(input(f"{rojoIntenso}Credito invalido! tu credito actual es de ${creditoAc}: {cerrarColor}"))
    return credito
        

    


def juego1(): 
    global archivoLogJug, archivoLogCat
    print(f"{amarillo}\nMayor o Menor{cerrarColor}")
    cerrar = cerrarJuego("", "Mayor o Menor")
    if (cerrar == "n"): 
        mensajeAnimado("saliendo", rojoIntenso)
    else: 
        posicion = iniciarJuego()
        archivoLogJug.seek(posicion, 0)
        jugador = pickle.load(archivoLogJug)
        desformatearJug(jugador)
        print(f"{amarillo}Hola!: {jugador.Nombre}{cerrarColor}")
        input(f"----dale enter para iniciar la partida----")
        while cerrar != "n": 
                creditoActual = jugador.Creditos
                if(creditoActual > 0.0):
                        
                        credito = validarCredito(creditoActual)
                        numeroC = menuCategorias()
                        if(numeroC == -1): 
                           cerrar = "n"
                           continuar()
                        else: 
                            opcionesDeCat = array(None, 6)
                            cantidadOpciones = obtenerOpciones(numeroC, opcionesDeCat)                 
                            jugar = "s"
                            while cantidadOpciones < 6 and jugar != "n": 
                                limpiarPantalla()
                                print(f"{rojoIntenso}esta categoria no tiene suficientes opciones!{cerrarColor}")
                                seguir = input("desea legir otra categoria? s / n: ")
                                if(seguir == "n"): 
                                    jugar = "n"
                                    cerrar = "n"  
                                else: 
                                    numeroC = menuCategorias()
                                    cantidadOpciones = obtenerOpciones(numeroC, opcionesDeCat)
                                           
                            if(jugar == "s"):
                                jugador.Juegos[0][0] = jugador.Juegos[0][0] + 1
                                posCat = busCategoriaDic(numeroC)
                                archivoLogCat.seek(posCat, 0)
                                categoriaAct = pickle.load(archivoLogCat)
                                desformatearCat(categoriaAct)
                                posicion1 = aleatorio.randint(0, 5)
                                campeon = opcionesDeCat[posicion1]
                                opcionesDeCat[posicion1] = None
                                aciertos = 0
                                i = 0
                                while i < 5:
                                            limpiarPantalla()
                                            print(f"{azul}Categoria: {categoriaAct.NombreCategoria}{cerrarColor}")
                                        
                                            posicion2 = aleatorio.randint(0, 5)
                                    
                                            
                                            if opcionesDeCat[posicion2] != None:
                                    
                                                retador = opcionesDeCat[posicion2]
                                    
                                            
                                                opcionesDeCat[posicion2] = None
                                    
                                                print()
                                                print(f"{amarillo}Ronda {i + 1} de 5{cerrarColor}")
                                    
                                                print(f" {verde} [1] {campeon.objeto}{cerrarColor}")
                                                print(f" {verde} [2] {retador.objeto}{cerrarColor}")
                                    
                                                eleccion = int(input(f"{rosa}¿{categoriaAct.Pregunta}? (Ingresa 1 o 2): {cerrarColor}"))
                                    
                                                while eleccion != 1 and eleccion != 2:
                                                    eleccion = int(input(f"{rojoError}Opción inválida. Ingresa 1 o 2: {cerrarColor}"))
                                    
                                                
                                                if categoriaAct.Tipo == 1:

                                                    if campeon.valor >= retador.valor:
                                                        ganadorReal = campeon
                                                        opcionCorrecta = 1
                                                    else:
                                                        ganadorReal = retador
                                                        opcionCorrecta = 2

                                                else:

                                                    if campeon.valor <= retador.valor:
                                                        ganadorReal = campeon
                                                        opcionCorrecta = 1
                                                    else:
                                                        ganadorReal = retador
                                                        opcionCorrecta = 2
                                    
                                                print()
                                                print(f"{amarillo}--- Resultado ---{cerrarColor}")
                                    
                                                print(f"{azul}• {campeon.objeto}: {campeon.valor:,}{cerrarColor}")
                                                print(f"{azul}• {retador.objeto}: {retador.valor:,}{cerrarColor}")
                                    
                                            
                                                if eleccion == opcionCorrecta:
                                    
                                                    print(f"{verde}¡Correcto! Acertaste.{cerrarColor}")
                                    
                                                    aciertos += 1
                                    
                                                else:
                                    
                                                    print(f"{rojoNormal}¡Fallaste!{cerrarColor}")
                                    
                                            
                                                campeon = ganadorReal
                                    
                                                i += 1
                                                print(F"{amarillo}La respuesta correcta era: {campeon.objeto}{cerrarColor}")
                                                input(f"{blanco}----presiona enten para continuar----{cerrarColor}")
                                            
                                                
                                    
                                print()
                                    
                                print(f"{amarillo}¡Juego terminado!{cerrarColor}")
                                print(f"{rosa}Tus aciertos totales: {aciertos} de 5{cerrarColor}")
                                
                                if(aciertos >= 4): 
                                        animacion(jugador.Nombre, "ganaste!", "gano")
                                        jugador.Creditos = creditoActual + credito
                                        jugador.Juegos[0][1] = jugador.Juegos[0][1] + 1
                                else: 
                                        animacion(jugador.Nombre, "perdiste", "perdio")
                                        jugador.Creditos = creditoActual - credito
                                        jugador.Juegos[0][2] = jugador.Juegos[0][2] + 1
                                cerrar = cerrarJuego(jugador.Nombre, "Mayor o Menor")
                                if cerrar == "n":
                                            mensajeAnimado("saliendo", rojoIntenso)
                                else:
                                            limpiarPantalla()
                            else: 
                                mensajeAnimado("saliendo", rojoIntenso)
                else:
                            print(f"{rojoNormal}{jugador.Nombre} No tienes mas credito para jugar.{cerrarColor}")
                            input(f"{blanco}---presiona enter para salir---{cerrarColor}")
                            mensajeAnimado("saliendo", rojoIntenso)
                            cerrar = "n"
        guardar(jugador, posicion)
        
def juego2(): 
    global archivoLogJug
    limpiarPantalla()
    print(f"{rosa}\nNumero Secreto{cerrarColor}")
    cerrar = cerrarJuego("", "Numero Secreto")
    if(cerrar == "n"): 
            mensajeAnimado("saliendo", rojoIntenso)
            
    else: 
        posicion = iniciarJuego()
        archivoLogJug.seek(posicion, 0)
        jugador = pickle.load(archivoLogJug)
        desformatearJug(jugador)
        print(f"{amarillo}Hola!: {jugador.Nombre}{cerrarColor}")
        input(f"----dale enter para iniciar la partida----")
       
        while (cerrar != "n"):
            limpiarPantalla()
            jugador.Juegos[1][0] = jugador.Juegos[1][0] + 1
            numeroSec = int(aleatorio.randint(1, 100))
            intentos = 6
            
            while (intentos != 0 and numeroSec != 0):
             
                try:
                    numero = int(input(f"\n{rosa}Ingrese un numero del 1 al 100 - Te quedan {intentos} intentos.{cerrarColor}  "))
                except ValueError:
                    print(f"{rojoError}\nError - Ingrese un numero correcto:{cerrarColor} ")
                    continue
                
                while (numero <= 0 or numero > 100):
                    numero = int(input(f"{rojoError}\nError - Ingrese un valor correcto:{cerrarColor} ").isdigit())

                if (numero > numeroSec):
                    print(f"{rojoNormal}\nES MENOR{cerrarColor}")
                    intentos -= 1
                elif (numero < numeroSec):
                    print(f"{rojoNormal}\nES MAYOR{cerrarColor}")
                    intentos -= 1

                else:
                    print(f"{verde}\nAcertaste el numero es {numeroSec} en el intento - {6 - intentos}.{cerrarColor}")
                    animacion(jugador.nombre, "acertaste!", "gano")
                    jugador.Juegos[1][1] = jugador.Juegos[1][1] + 1
                    numeroSec = 0
                    
                if(intentos == 0):
                    print(f"{rojoNormal}\nPerdiste el juego. El numero secreto era {numeroSec}.{cerrarColor}")
                    animacion(jugador.Nombre, "Perdiste!!!", "perdio")
                    jugador.Juegos[1][2] = jugador.Juegos[1][2] + 1
                   
                
            cerrar = cerrarJuego(jugador.Nombre, "Numero Secreto")
            if cerrar == "n":
                mensajeAnimado("saliendo", rojoIntenso)
            else:
                limpiarPantalla()
        guardar(jugador, posicion)
       
# ================ BLACK JACK =================
# CREAR BARAJA Y MEZCLAR BARAJA
def crearMazo(mazo):
    palos = array(0, 4)
    for i in range(len(palos)): 
        palos[i] = i
    fila = 0
    for i in range(len(palos)):
        for j in range(1,14):
            mazo[fila][0] = j
            mazo[fila][1] = palos[i]
            fila += 1
            
#MEZCLAR CARTAS
def mezclarMazo(mazo):
   
    mensajeAnimado("\nIniciando partida", amarillo)
    tamaño = len(mazo)
    for i in range(tamaño):
        posicion = aleatorio.randint(0, tamaño - 1)
        aux = mazo[i][0]
        mazo[i][0] = mazo[posicion][0]
        mazo[posicion][0] = aux

# PEDIR CARTA
def pedirCarta(mazo):
    posicion = aleatorio.randint(0, len(mazo)-1)
    while mazo[posicion][0] == 0:
        posicion = aleatorio.randint(0, len(mazo)-1)
    carta = [
        mazo[posicion][0],
        mazo[posicion][1]
    ]
    mazo[posicion][0] = 0
    mazo[posicion][1] = 0
    return carta

# AGREGAMOS CARTA AL MAZO 
def agregarCarta(mano, carta, tamaño):
    i = 0
    while i < tamaño:
        if mano[i][0] == 0:
            mano[i][0] = carta[0]
            mano[i][1] = carta[1]
            return
        i += 1

# CONTAR PUNTOS
def contarPuntos(cartas):
    puntos = 0
    ases = 0
    for i in range(len(cartas)):
        valor = cartas[i][0]
        if valor != 0:
            if valor == 1:
                puntos += 11
                ases += 1
            elif valor >= 11:
                puntos += 10
            else:
                puntos += valor
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
    return puntos

#DIBUJAR LA CARTA TAPADA
def dibujarCartaTapada():
    dibujo = [

        f"{blanco}{negro}┌───────────┐{cerrarColor}",
        f"{blanco}{negro}│░░░░░░░░░░░│{cerrarColor}",
        f"{blanco}{negro}│░░░░░░░░░░░│{cerrarColor}",
        f"{blanco}{negro}│░░░░░░░░░░░│{cerrarColor}",
        f"{blanco}{negro}│░░░░░░░░░░░│{cerrarColor}",
        f"{blanco}{negro}│░░░░░░░░░░░│{cerrarColor}",
        f"{blanco}{negro}└───────────┘{cerrarColor}"

    ]
    return dibujo

# DIBUJAR LAS CARTAS
def dibujarCarta(mano, tapada):

    cartas = matriz(7, len(mano), "")

    for i in range(len(mano)):

        if mano[i][0] != 0:

            if tapada and i == 1:
                dibujo = dibujarCartaTapada()

            else:
                valor = mano[i][0]
                palo = mano[i][1]

                if valor == 1:
                    valorCarta = "A"
                elif valor == 11:
                    valorCarta = "J"
                elif valor == 12:
                    valorCarta = "Q"
                elif valor == 13:
                    valorCarta = "K"
                else:
                    valorCarta = valor

                if palo == 0:
                    simbolo = "♠"
                elif palo == 1:
                    simbolo = "♥"
                elif palo == 2:
                    simbolo = "♣"
                else:
                    simbolo = "♦"


                if palo == 1 or palo == 3:
                    colorCarta = rojoNormal
                else:
                    colorCarta = negro


                dibujo = [
                    f"{blanco}{colorCarta}┌───────────┐{cerrarColor}",
                    f"{blanco}{colorCarta}│ {valorCarta:<2}        │{cerrarColor}",
                    f"{blanco}{colorCarta}│           │{cerrarColor}",
                    f"{blanco}{colorCarta}│     {simbolo}     │{cerrarColor}",
                    f"{blanco}{colorCarta}│           │{cerrarColor}",
                    f"{blanco}{colorCarta}│        {valorCarta:>2} │{cerrarColor}",
                    f"{blanco}{colorCarta}└───────────┘{cerrarColor}"
                ]


            for j in range(7):
                cartas[j][i] = dibujo[j]


    for fila in range(7):
        linea = ""
        for columna in range(len(mano)):
            linea += cartas[fila][columna] + " "
        print(linea)

# TURNO DEL JUGADOR
def turnoJugador(cJugador, cBanca, mazo):
    limpiarPantalla()
    print(f"\n{azul}TURNO DEL JUGADOR{cerrarColor}")
    carta1 = pedirCarta(mazo)
    carta2 = pedirCarta(mazo)
    agregarCarta(cJugador, carta1, 8)
    agregarCarta(cJugador, carta2, 8)
    print("\nCartas de la banca:")
    dibujarCarta(cBanca, True)
    print("\nTus cartas:")
    dibujarCarta(cJugador, False)
    puntosJugador = contarPuntos(cJugador)
    print("\nPuntos del jugador: ", puntosJugador)
    if puntosJugador == 21:
        print("llegaste a 21!")
        time.sleep(0.5)
        return puntosJugador
    while puntosJugador < 21:
        pregunta = input("\n¿Deseas pedir carta? (s/n) ").lower().strip()
        while pregunta != "s" and pregunta != "n":
            pregunta = input(f"{rojoError}\nError - Ingrese nuevamente s/n: {cerrarColor}").lower().strip()
        if pregunta == "n":
            return puntosJugador
        elif pregunta == "s":
            limpiarPantalla()
            print(f"\n{azul}TURNO DEL JUGADOR{cerrarColor}")
            carta = pedirCarta(mazo)
            agregarCarta(cJugador, carta, 8)
            print("\nCartas banca:")
            dibujarCarta(cBanca, True)
            print("\nTus cartas:")
        
            time.sleep(0.5)
            dibujarCarta(cJugador, False)
            puntosJugador = contarPuntos(cJugador)
            print("\nPuntos del jugador: ", puntosJugador)
    return puntosJugador

# TURNO DE LA BANCA
def turnoBanca(cBanca, cJugador, mazo):
    limpiarPantalla()
    print(f"{verde}\nTURNO DE LA BANCA{cerrarColor}")
    print("\nTus cartas:")
    dibujarCarta(cJugador, False)
    print("\nCartas de la banca:")
    dibujarCarta(cBanca, False)
    puntosBanca = contarPuntos(cBanca)
    print("\nPuntos de la banca: ", puntosBanca)
    time.sleep(2)
    while puntosBanca < 17:
        carta = pedirCarta(mazo)
        agregarCarta(cBanca, carta, 8)
        limpiarPantalla()
        print(f"{verde}\nTURNO DE LA BANCA{cerrarColor}")
        print("\nTus cartas:")
        dibujarCarta(cJugador, False)
        print("\nCartas de la banca:")
    
        time.sleep(0.5)
        dibujarCarta(cBanca, False)
        puntosBanca = contarPuntos(cBanca)
        print("\nPuntos de la banca: ", puntosBanca)
        time.sleep(0.5)
    if puntosBanca >= 17 and puntosBanca <= 21:
        print(f"\nLa banca se planta con {puntosBanca} puntos")
        time.sleep(0.5)
    elif puntosBanca > 21:
        print(f"\nLa banca se pasó de 21 con {puntosBanca} puntos")
        time.sleep(0.5)
    return puntosBanca


def juego3():
    global archivoLogJug
    
    limpiarPantalla()
    print(f"{amarillo}\nBlack Jack{cerrarColor}")
    cerrar = cerrarJuego("", "Black Jack")
    if(cerrar == "n"): 
        mensajeAnimado("saliendo", rojoIntenso)
    else: 
        posicion = iniciarJuego()
        archivoLogJug.seek(posicion, 0)
        jugador = pickle.load(archivoLogJug)
        desformatearJug(jugador)
        print(f"{amarillo}Hola!: {jugador.Nombre}{cerrarColor}")
        input(f"----dale enter para iniciar la partida----")
        while cerrar != "n":
            jugador.Juegos[2][0] = jugador.Juegos[2][0] + 1
            mazo = matriz(52,2,0)
            crearMazo(mazo)
            mezclarMazo(mazo)
            cJugador = matriz(8,2,0)
            cBanca = matriz(8,2,0)
            carta1 = pedirCarta(mazo)
            carta2 = pedirCarta(mazo)
            agregarCarta(cBanca, carta1, 8)
            agregarCarta(cBanca, carta2, 8)
            puntosJugador = turnoJugador(cJugador,cBanca,mazo)
            if puntosJugador > 21:
                jugador.Juegos[2][2] = jugador.Juegos[2][2] + 1
                animacion(jugador.Nombre,"te pasaste de 21","perdio")
            else:
                puntosBanca = turnoBanca(cBanca,cJugador,mazo)
                print(f"\n{verde}Jugador: {puntosJugador} {cerrarColor}")
                print(f"\n{azul}Banca: {puntosBanca} {cerrarColor}")
                if puntosBanca > 21 or puntosJugador > puntosBanca:
                    jugador.Juegos[2][1] = jugador.Juegos[2][1] + 1
                    animacion(jugador.Nombre,"ganaste","gano")
                elif puntosBanca > puntosJugador:
                    jugador.Juegos[2][2] = jugador.Juegos[2][2] + 1
                    animacion(jugador.Nombre,"perdiste","perdio")
                else:
                    print("Empate")
            
            cerrar = cerrarJuego(jugador.Nombre,"Black Jack")
            if cerrar == "n":
                mensajeAnimado("Saliendo", rojoError)
            else:
                limpiarPantalla()
        guardar(jugador, posicion)

       
       
        
def juego4():   
    global archivoLogJug

    limpiarPantalla()

    print(f"{azul}\nPar o Impar{cerrarColor}")
    
    cerrar = cerrarJuego("", "Par o Impar")
    if(cerrar == "n"): 
        mensajeAnimado("saliendo", rojoIntenso)
    
    else: 
        posicion = iniciarJuego()
        archivoLogJug.seek(posicion, 0)
        jugador = pickle.load(archivoLogJug)
        desformatearJug(jugador)
        print(f"{amarillo}Hola!: {jugador.Nombre}{cerrarColor}")
        input(f"----dale enter para iniciar la partida----")
                

        while (cerrar != "n"):
            limpiarPantalla()
            jugador.Juegos[3][0] = jugador.Juegos[3][0] + 1
            creditoActual = jugador.Creditos
            
            

            if creditoActual > 0.0:
                        
                
               
                numero1 = int(aleatorio.randint(1, 6))
                numero2 = int(aleatorio.randint(1, 6))
                suma = numero1 + numero2
                par = suma % 2

               
                apuesta = validarCredito(creditoActual)
                mensajeAnimado(f"tirando dados", azul)

                pregunta = str(input(f"{azul}\n\nDecir si es Par o Impar: {cerrarColor}")).lower().strip()
                while(pregunta != "par" and pregunta != "impar"):
                    pregunta = str(input(f"{rojoError}\nError - Ingrese nuevamente:{cerrarColor} ")).lower().strip()




                if (pregunta == "par"):
                    if (par == 0):
                        print(f"\n{verde}Ganaste!!! - La suma de los dados es {suma}.{cerrarColor}")
                        animacion(jugador.Nombre, " ganaste !!!!", "gano")
                        jugador.Juegos[3][1] = jugador.Juegos[3][1] + 1
                        jugador.Creditos = jugador.Creditos + apuesta
                    
                    else:
                        print(f"\n{rojoNormal}Perdiste!!! - La suma de los dados es {suma}.{cerrarColor}")
                        animacion(jugador.Nombre, " perdiste !!!!", "perdio")
                        jugador.Juegos[3][2] = jugador.Juegos[3][2] + 1
                        jugador.Creditos = jugador.Creditos - apuesta
                       
                elif (pregunta == "impar"):
                    if (par == 1):
                        print(f"\n{verde}Ganaste!!! - La suma de los dados es {suma}.{cerrarColor}")
                        animacion(jugador.Nombre, " ganaste !!!!", "gano")
                        jugador.Juegos[3][1] = jugador.Juegos[3][1] + 1
                        jugador.Creditos = jugador.Creditos + apuesta
                        
                    else:
                        print(f"\n{rojoNormal}Perdiste!!! - La suma de los dados es {suma}.{cerrarColor}")
                        animacion(jugador.Nombre, " perdiste !!!!", "perdio")
                        jugador.Juegos[3][2] = jugador.Juegos[3][2] + 1
                        jugador.Creditos = jugador.Creditos - apuesta
                        
                    
                cerrar = cerrarJuego(jugador.Nombre, "Par e Impar")
                if cerrar == "n":
                    mensajeAnimado("saliendo", rojoIntenso)
                else:
                    limpiarPantalla()
            else:
                print(f"\n{rojoNormal}No tiene mas credito para jugar.{cerrarColor}")
                mensajeAnimado("saliendo", rojoIntenso)
                cerrar = "n"
        guardar(jugador, posicion)


def ordenarPorCreditos():

    global archivoFisJug, archivoLogJug
    archivoLogJug.seek (0, 0)
    tamArch = os.path.getsize(archivoFisJug)

    aux = pickle.load(archivoLogJug)
    tamReg = archivoLogJug.tell() 
  
    cantReg = tamArch // tamReg  
    for i in range(0, cantReg-1):
            for j in range(i+1, cantReg):
                archivoLogJug.seek(i*tamReg, 0)
                auxi = pickle.load(archivoLogJug)
               
                archivoLogJug.seek(j*tamReg, 0)
                auxj = pickle.load(archivoLogJug)
               
                if float(auxi.Creditos.strip()) < float(auxj.Creditos.strip()):
                    archivoLogJug.seek(i*tamReg, 0)
                    pickle.dump(auxj, archivoLogJug)
                    archivoLogJug.seek(j*tamReg, 0)
                    pickle.dump(auxi, archivoLogJug)
                    archivoLogJug.flush()
    

def listarJugadores():
    global archivoFisJug, archivoLogJug
    limpiarPantalla()

    tamArch = os.path.getsize(archivoFisJug)

    if tamArch > 0:
        ordenarPorCreditos()
        archivoLogJug.seek(0, 0)
        aux = pickle.load(archivoLogJug)
        tamReg = archivoLogJug.tell()

        cantReg = tamArch // tamReg

        print(f"\n{azul}══════════════════════════════════════════════{cerrarColor}")
        print(f"{amarillo}              LISTA DE JUGADORES{cerrarColor}")
        print(f"{azul}══════════════════════════════════════════════{cerrarColor}")

        print(f"{amarillo}{'Jugador':<30} {'Créditos':>13}{cerrarColor}")
        print(f"{azul}──────────────────────────────────────────────{cerrarColor}")

        archivoLogJug.seek(0, 0)

        for i in range(cantReg):

            jugador = pickle.load(archivoLogJug)

            desformatearJug(jugador)

            if jugador.Creditos < 1000:
                colorCredito = rojoIntenso

            elif jugador.Creditos <= 5000:
                colorCredito = amarillo

            else:
                colorCredito = verde

            print(f"{rosa}[{i + 1}]{cerrarColor} "
                  f"{amarillo}{jugador.Nombre:<30}{cerrarColor} "
                  f"{colorCredito}${jugador.Creditos:>10.2f}{cerrarColor}")

        print(f"{azul}══════════════════════════════════════════════{cerrarColor}")

    else:
        print(f"{rojoNormal}No hay jugadores cargados.{cerrarColor}")

    continuar()
        
def mostrarEstadisticas(pos):  
    global archivoLogJug, archivoFisJug
    limpiarPantalla()
    archivoLogJug.seek(pos, 0)

    jugador = pickle.load(archivoLogJug)

    desformatearJug(jugador)

    nombre = jugador.Nombre
    print(f"{amarillo}ESTADISTICAS DE {nombre}{cerrarColor}")
    print()

    print("\033[1;36m╔════════════════════╦══════════╦══════════╦══════════╗\033[0m")
    print("\033[1;36m║\033[1;37m JUEGO              \033[1;36m║\033[1;33m JUGADOS  \033[1;36m║\033[1;32m GANADOS  \033[1;36m║\033[1;31m PERDIDOS \033[1;36m║\033[0m")
    print("\033[1;36m╠════════════════════╬══════════╬══════════╬══════════╣\033[0m")

    # Mayor o Menor
    print("\033[1;36m║\033[0m \033[1;32m{:<18}\033[0m \033[1;36m║\033[1;33m {:>8} \033[1;36m║\033[1;32m {:>8} \033[1;36m║\033[1;31m {:>8} \033[1;36m║\033[0m".format(
        "Mayor o Menor",
        jugador.Juegos[0][0],
        jugador.Juegos[0][1],
        jugador.Juegos[0][2]
    ))

    # Número Secreto
    print("\033[1;36m║\033[0m \033[1;33m{:<18}\033[0m \033[1;36m║\033[1;33m {:>8} \033[1;36m║\033[1;32m {:>8} \033[1;36m║\033[1;31m {:>8} \033[1;36m║\033[0m".format(
        "Número Secreto",
        jugador.Juegos[1][0],
        jugador.Juegos[1][1],
        jugador.Juegos[1][2]
    ))

    # Blackjack
    print("\033[1;36m║\033[0m \033[1;35m{:<18}\033[0m \033[1;36m║\033[1;33m {:>8} \033[1;36m║\033[1;32m {:>8} \033[1;36m║\033[1;31m {:>8} \033[1;36m║\033[0m".format(
        "Blackjack",
        jugador.Juegos[2][0],
        jugador.Juegos[2][1],
        jugador.Juegos[2][2]
    ))

    # Par o Impar
    print("\033[1;36m║\033[0m \033[1;34m{:<18}\033[0m \033[1;36m║\033[1;33m {:>8} \033[1;36m║\033[1;32m {:>8} \033[1;36m║\033[1;31m {:>8} \033[1;36m║\033[0m".format(
        "Par o Impar",
        jugador.Juegos[3][0],
        jugador.Juegos[3][1],
        jugador.Juegos[3][2]
    ))

    print("\033[1;36m╚════════════════════╩══════════╩══════════╩══════════╝\033[0m")

    continuar()

def mostrarJugador(): 
    global archivoFisJug
    t = os.path.getsize(archivoFisJug)
    if(t == 0): 
        print(f"{rojoNormal}no hay jugadores registrados...{cerrarColor}")
        continuar()
    else: 
        nombre = ""
        while nombre != "*": 
            limpiarPantalla()
            print(f"{amarillo}BUSCAR JUGADOR{cerrarColor}")
            nombre = str(input("ingrese el nombre del jugador o (*) para salir: "))
            if(nombre != "*"): 
                pos = buscarJugador(nombre)
                if(pos != -1): 
                    mostrarEstadisticas(pos)
                else: 
                    print(f"{rojoIntenso}no se encontro el jugador, ingresa uno valido!{cerrarColor}")
                    time.sleep(3)
        
    
def menuReporte(): 
        limpiarPantalla()
        print(f"{rosa}REPORTE{cerrarColor}")
        print(f"{verde}a. Lista de jugadores{cerrarColor}")
        print(f"{amarillo}b. Buscar jugador{cerrarColor}")
        print(f"{rojoNormal}c. volver{cerrarColor}")
        
def reporte(): 
    op = ""
    while op != "c": 
        menuReporte()
        op = input("ingresa una opcion: ")
        if op == "a": 
            limpiarPantalla()
            listarJugadores()
        elif(op == "b"): 
            limpiarPantalla()
            mostrarJugador()
        elif(op == "c"): 
            mensajeAnimado("Saliendo", rojoError)




def cartel():
    
   
    
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
        


          
    
    continuar = str(input("Ingrese ENTER para entrar".center(50, "-")))
    while(continuar != ""): 
        continuar = str(input(f"{rojoError}Error - Ingrese ENTER para entrar{cerrarColor}".center(50, "-"))) 

def despedida():
    limpiarPantalla()
    print(f"""{rojoIntenso}
    ╔════════════════════════════════════════════╗
    ║              🎰 CASINO ROYAL 🎰           ║
    ║                                            ║
    ║              ¡GRACIAS POR JUGAR!           ║
    ║                                            ║
    ║        NO APUESTE, JUEGA POR DIVERSIÓN     ║
    ║                                            ║
    ║           PRESIONE ENTER PARA SALIR        ║
    ╚════════════════════════════════════════════╝
    {cerrarColor}""")
    continuar()
    limpiarPantalla()



def menu(): 
    global archivoLogJug, archivoLogCat, archivoLogOpc
    contrasena = "admin1234"

    opcion1 = ""
    while opcion1 != "G": 
        menuop()
        opcion1 = str(input("ingrese una opcion: ")).upper()
        if(opcion1 == "A"): 
            limpiarPantalla()
            juego1()
        elif(opcion1 == "B"): 
            juego2()
        elif(opcion1 == "C"): 
            juego3()
        elif(opcion1 == "D"): 
            juego4()
        elif(opcion1 == "E"): 
            reporte()
        elif(opcion1 == "F"): 
            limpiarPantalla()
            verificar(contrasena)
        elif(opcion1 == "G"): 
            # mensajeAnimado("cerrando sesion", rojoIntenso)
            archivoLogOpc.close()
            archivoLogCat.close()
            archivoLogJug.close()
            despedida()
            






def inicio(ruta): 
    if(os.path.exists(ruta)): 
        archivo = open(ruta, "r+b")
    else: 
        archivo = open(ruta, "w+b")
    return archivo

archivoFisJug = "./archivos/jugadores.dat"
archivoFisCat = "./archivos/categorias.dat"
archivoFisOpc = "./archivos/opciones.dat"

archivoLogJug = inicio(archivoFisJug)
archivoLogCat = inicio(archivoFisCat)
archivoLogOpc = inicio(archivoFisOpc)


color()
cartel()
menu()
