
from constantes import *
from plataforma import Plataform
import json

def readJson(file):
        with open(file, 'r') as f:
            data = json.load(f)
        return data
def import_platforms():

    platform_list = []
    #PLATAFORMAS LOW LEVEL/MID LEVEL
    platform_list.append(Plataform(x=400,y=600,width=50,height=50,type=0))
    platform_list.append(Plataform(x=450,y=600,width=50,height=50,type=1))
    platform_list.append(Plataform(x=500,y=600,width=50,height=50,type=2))   
    platform_list.append(Plataform(x=600,y=530,width=50,height=50,type=12))
    platform_list.append(Plataform(x=650,y=530,width=50,height=50,type=14))
    platform_list.append(Plataform(x=750,y=460,width=50,height=50,type=12))
    platform_list.append(Plataform(x=800,y=460,width=50,height=50,type=13))
    platform_list.append(Plataform(x=850,y=460,width=50,height=50,type=13))
    platform_list.append(Plataform(x=900,y=460,width=50,height=50,type=14))
    platform_list.append(Plataform(x=0,y=460,width=150,height=50,type=13))
    platform_list.append(Plataform(x=0,y=460,width=150,height=50,type=13))
    platform_list.append(Plataform(x=150,y=460,width=100,height=50,type=14))
    platform_list.append(Plataform(x=-17,y=0,width=20,height=1000,type=15))
    platform_list.append(Plataform(x=1350,y=460,width=150,height=50,type=13))
    platform_list.append(Plataform(x=1200,y=460,width=150,height=50,type=12))
    platform_list.append(Plataform(x=1200,y=460,width=150,height=50,type=12))
    #PLATAFORMAS MEDIO SALTO A ARRIBA/MEDIO SALTO ABAJO
    platform_list.append(Plataform(x=770,y=320,width=50,height=30,type=0))
    platform_list.append(Plataform(x=820,y=320,width=50,height=30,type=1))
    platform_list.append(Plataform(x=870,y=320,width=50,height=30,type=2))

    platform_list.append(Plataform(x=240,y=550,width=30,height=40,type=0))
    platform_list.append(Plataform(x=270,y=550,width=30,height=40,type=1))
    platform_list.append(Plataform(x=300,y=550,width=30,height=40,type=2))

    platform_list.append(Plataform(x=1085,y=320,width=30,height=30,type=0))
    platform_list.append(Plataform(x=1115,y=320,width=30,height=30,type=1))
    platform_list.append(Plataform(x=1145,y=320,width=30,height=30,type=2))
    #PLATAFORMAS ARRIBA DER
    platform_list.append(Plataform(x=0,y=180,width=150,height=45,type=13))
    platform_list.append(Plataform(x=150,y=180,width=160,height=45,type=14))
    #PLATAFORMAS ARRIBA MID
    platform_list.append(Plataform(x=450,y=180,width=160,height=45,type=12))
    platform_list.append(Plataform(x=600,y=180,width=150,height=45,type=13))
    platform_list.append(Plataform(x=750,y=180,width=150,height=45,type=13))
    platform_list.append(Plataform(x=900,y=180,width=160,height=45,type=14))
    #PLATAFORMAS ARRIBA IZQ
    platform_list.append(Plataform(x=1200,y=180,width=150,height=45,type=12))
    platform_list.append(Plataform(x=1350,y=180,width=160,height=45,type=13))

    return platform_list