from math import fabs
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Caballo:
    def __init__(self, id):
        self._no_caballo = id
        self._vel_caballo = random.randrange(20, 35)
    def imprimir(self):
        print('ID: {}\nVelocidad: {} km/h'.format(self._no_caballo,self._vel_caballo))
    @property
    def vel_caballo(self):
        return self._vel_caballo
    @property
    def no_caballo(self):
        return self._no_caballo
class Coordenadas:
    def _init_(self, x, y):
        self.x = x
        self.y = y
Grafos = nx.Graph()
ccaballo = []
def Crear_Caballos():
    for n in range(1,26):
        horse = Caballo(n)
        ccaballo.append(horse)
grupos = []
def Clasificacion():
    con = 0
    for i in range(0, 25, 5):
        pivot = []
        for j in range(0,5):
            pivot.append(ccaballo[j+i])
        pivot.sort(key=lambda x: x.vel_caballo)
        grupos.append(pivot)
def Eliminatoria():
    pivot = []        
    for o in range(len(grupos)):
        pivot.append(grupos[o][4])
    pivot.sort(key=lambda x: x.vel_caballo)
    print('Los caballos mas rapidos son:')
    #pivot[4].imprimir()
    #pivot[3].imprimir()

def Graficacion():
    #Grafos = nx.Graph()
    pivotf = []    
    vgrafos = []
    agrafos = []   
    posicion = {}
    for p in range(len(grupos)):                                #Convertimos la matriz en un arreglo unidimensional
        for q in range(0,5):
            pivotf.append(grupos[p][q])
    pivotf.sort(key=lambda x: x.vel_caballo)
    for r in range(0,25):                                       #For para generar los vertices
        vgrafos.append(pivotf[r].no_caballo)
        #print(r)                                               Print para probar funcionamiento
        #pivotf[r].imprimir()
    Grafos.add_nodes_from(vgrafos)
    agrafos = [(pivotf[24].no_caballo, pivotf[23].no_caballo), (pivotf[23].no_caballo, pivotf[22].no_caballo), (pivotf[22].no_caballo, pivotf[21].no_caballo), (pivotf[21].no_caballo, pivotf[20].no_caballo),
         (pivotf[20].no_caballo, pivotf[19].no_caballo), (pivotf[19].no_caballo, pivotf[18].no_caballo), (pivotf[18].no_caballo, pivotf[17].no_caballo), (pivotf[17].no_caballo, pivotf[16].no_caballo),
         (pivotf[16].no_caballo, pivotf[15].no_caballo), (pivotf[15].no_caballo, pivotf[14].no_caballo), (pivotf[14].no_caballo, pivotf[13].no_caballo), (pivotf[13].no_caballo, pivotf[12].no_caballo),
        (pivotf[12].no_caballo, pivotf[11].no_caballo), (pivotf[11].no_caballo, pivotf[10].no_caballo), (pivotf[10].no_caballo, pivotf[9].no_caballo), (pivotf[9].no_caballo, pivotf[8].no_caballo), 
        (pivotf[8].no_caballo, pivotf[7].no_caballo), (pivotf[7].no_caballo, pivotf[6].no_caballo), (pivotf[6].no_caballo, pivotf[5].no_caballo), (pivotf[5].no_caballo, pivotf[4].no_caballo),
        (pivotf[4].no_caballo, pivotf[3].no_caballo), (pivotf[3].no_caballo, pivotf[2].no_caballo), (pivotf[2].no_caballo, pivotf[1].no_caballo), (pivotf[1].no_caballo, pivotf[0].no_caballo)]
    Grafos.add_edges_from(agrafos)
    posicion = {pivotf[0].no_caballo: (0, 35), pivotf[1].no_caballo: (5, 35), pivotf[2].no_caballo: (10, 35), pivotf[3].no_caballo: (15, 35), pivotf[4].no_caballo: (20, 35),
                pivotf[5].no_caballo: (0, 30), pivotf[6].no_caballo: (5, 30), pivotf[7].no_caballo: (10, 30), pivotf[8].no_caballo: (15, 30), pivotf[9].no_caballo: (20, 30), 
                pivotf[10].no_caballo: (0, 25), pivotf[11].no_caballo: (5, 25), pivotf[12].no_caballo: (10, 25), pivotf[13].no_caballo: (15, 25), pivotf[14].no_caballo: (20, 25),
                pivotf[15].no_caballo: (0, 20), pivotf[16].no_caballo: (5, 20), pivotf[17].no_caballo: (10, 20), pivotf[18].no_caballo: (15, 20), pivotf[19].no_caballo: (20, 20),
                pivotf[20].no_caballo: (0, 15), pivotf[21].no_caballo: (5, 15), pivotf[22].no_caballo: (10, 15), pivotf[23].no_caballo: (15, 15), pivotf[24].no_caballo: (20, 15)}
        
    puntoA = Coordenadas()
    puntoA.x = posicion[pivotf[24].no_caballo][0]
    puntoA.y = posicion[pivotf[24].no_caballo][1]
    puntoB = Coordenadas()
    puntoB.x = posicion[pivotf[23].no_caballo][0]
    puntoB.y = posicion[pivotf[23].no_caballo][1]
    puntoC = Coordenadas()
    puntoC.x = posicion[pivotf[22].no_caballo][0]
    puntoC.y = posicion[pivotf[22].no_caballo][1]
    puntoD = Coordenadas()
    puntoD.x = posicion[pivotf[21].no_caballo][0]
    puntoD.y = posicion[pivotf[21].no_caballo][1]
    puntoE = Coordenadas()
    puntoE.x = posicion[pivotf[20].no_caballo][0]
    puntoE.y = posicion[pivotf[20].no_caballo][1]
    puntoF = Coordenadas()
    puntoF.x = posicion[pivotf[19].no_caballo][0]
    puntoF.y = posicion[pivotf[19].no_caballo][1]
    puntoG = Coordenadas()
    puntoG.x = posicion[pivotf[18].no_caballo][0]
    puntoG.y = posicion[pivotf[18].no_caballo][1]
    puntoH = Coordenadas()
    puntoH.x = posicion[pivotf[17].no_caballo][0]
    puntoH.y = posicion[pivotf[17].no_caballo][1]
    puntoI = Coordenadas()
    puntoI.x = posicion[pivotf[16].no_caballo][0]
    puntoI.y = posicion[pivotf[16].no_caballo][1]
    puntoJ = Coordenadas()
    puntoJ.x = posicion[pivotf[15].no_caballo][0]
    puntoJ.y = posicion[pivotf[15].no_caballo][1]
    puntoK = Coordenadas()
    puntoK.x = posicion[pivotf[14].no_caballo][0]
    puntoK.y = posicion[pivotf[14].no_caballo][1]
    puntoL = Coordenadas()
    puntoL.x = posicion[pivotf[13].no_caballo][0]
    puntoL.y = posicion[pivotf[13].no_caballo][1]
    puntoM = Coordenadas()
    puntoM.x = posicion[pivotf[12].no_caballo][0]
    puntoM.y = posicion[pivotf[12].no_caballo][1]
    puntoN = Coordenadas()
    puntoN.x = posicion[pivotf[11].no_caballo][0]
    puntoN.y = posicion[pivotf[11].no_caballo][1]
    puntoO = Coordenadas()
    puntoO.x = posicion[pivotf[10].no_caballo][0]
    puntoO.y = posicion[pivotf[10].no_caballo][1]
    puntoP = Coordenadas()
    puntoP.x = posicion[pivotf[9].no_caballo][0]
    puntoP.y = posicion[pivotf[9].no_caballo][1]
    puntoQ = Coordenadas()
    puntoQ.x = posicion[pivotf[8].no_caballo][0]
    puntoQ.y = posicion[pivotf[8].no_caballo][1]
    puntoR = Coordenadas()
    puntoR.x = posicion[pivotf[7].no_caballo][0]
    puntoR.y = posicion[pivotf[7].no_caballo][1]
    puntoS = Coordenadas()
    puntoS.x = posicion[pivotf[6].no_caballo][0]
    puntoS.y = posicion[pivotf[6].no_caballo][1]
    puntoT = Coordenadas()
    puntoT.x = posicion[pivotf[5].no_caballo][0]
    puntoT.y = posicion[pivotf[5].no_caballo][1]
    puntoU = Coordenadas()
    puntoU.x = posicion[pivotf[4].no_caballo][0]
    puntoU.y = posicion[pivotf[4].no_caballo][1]
    puntoV = Coordenadas()
    puntoV.x = posicion[pivotf[3].no_caballo][0]
    puntoV.y = posicion[pivotf[3].no_caballo][1]
    puntoY = Coordenadas()
    puntoY.x = posicion[pivotf[2].no_caballo][0]
    puntoY.y = posicion[pivotf[2].no_caballo][1]
    puntoX = Coordenadas()
    puntoX.x = posicion[pivotf[1].no_caballo][0]
    puntoX.y = posicion[pivotf[1].no_caballo][1]
    puntoZ = Coordenadas()
    puntoZ.x = posicion[pivotf[0].no_caballo][0]
    puntoZ.y = posicion[pivotf[0].no_caballo][1]

    Puntos = {pivotf[24]: puntoA, pivotf[23]: puntoB, pivotf[22]: puntoC, pivotf[21]: puntoD, pivotf[20]: puntoE, 
            pivotf[19]: puntoF, pivotf[18]: puntoG, pivotf[17]: puntoH, pivotf[16]: puntoI, pivotf[15]: puntoJ, 
            pivotf[14]: puntoK, pivotf[13]: puntoL, pivotf[12]: puntoM, pivotf[11]: puntoN, pivotf[10]: puntoO, 
            pivotf[9]: puntoP, pivotf[8]: puntoQ, pivotf[7]: puntoR, pivotf[6]: puntoS, pivotf[5]: puntoT, 
            pivotf[4]: puntoU, pivotf[3]: puntoV, pivotf[2]: puntoY, pivotf[1]: puntoX, pivotf[0]: puntoZ}   
    nx.draw(Grafos, pos=posicion, node_color='gray', with_labels=True)  #Funcion para dibujar grafo
    plt.show()

Crear_Caballos()
Clasificacion()
Eliminatoria()
Graficacion()