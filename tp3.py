
import os, pickle

ArcFisJug = "jugadores.dat"

if not os.path.exists(ArcFisJug):

    ArcLogJug = open(ArcFisJug, "w+b")

    print("creado")

else:

    ArcLogJug = open(ArcFisJug, "r+b")

    print("ya existe")

