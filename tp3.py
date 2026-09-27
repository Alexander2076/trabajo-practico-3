
import os, picle

ArcFisiJug = "jugadores.dat"

if not os.path.exists(ArcFisiJug):

    ArcLogJug = open(ArcFisiJug, "w+b")

    print("creado")

else:

    ArcLogJug = open(ArcFisiJug, "r+b")

    print("ya existe")

