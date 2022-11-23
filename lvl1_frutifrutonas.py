from constantes import *
from fruits import Fruits



def import_fruits():

    frutonas_list = []
    frutonas_list.append(Fruits(x=500,y=550,frame_rate_ms=10,move_rate_ms=100,f_scale=0.5))
    frutonas_list.append(Fruits(x=100,y=400,frame_rate_ms=10,move_rate_ms=100,f_scale=0.5))
    
    return frutonas_list