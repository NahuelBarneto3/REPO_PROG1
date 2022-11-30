from enemigo import Enemy
import json
from constantes import *
from plataforma import Plataform
from enemigo import Enemy
from Attacking_Enemy import Attacking_Enemy
from fruits import Fruits
from player import Player
class LvlConfig():
    def __init__(self,lvl):
        self.lvl = lvl
        match(self.lvl):
            case 1:
                self.data = self.CargarJson(path_lvl_1)
                self.__screen = screen_lvl_1_path #constants 
                self.nivel = "nivel_uno"
                self.__player = Player(x=10,y=463,respawn_pos_x=10,respawn_pos_y=600,speed_walk=8,speed_run=12,gravity=16,jump_power=40,frame_rate_ms=20,move_rate_ms=20,jump_height=150,p_scale=0.2,interval_time_jump=400)
            case 2:
               # self.data = self.CargarJson(path_lvl_2)
               # self.__screen = screen_lvl_2_path #constants 
               pass


    def CargarJson(self,file):
        with open(file, 'r') as f:
            self.data = json.load(f)
        return self.data
    
    def get_platforms(self):
        
        platforms_list_dic = self.data[self.nivel]["platforms"]
        self.platform_list = []
        for platforms in platforms_list_dic:
            
            platform = Plataform(x=platforms["x"],y=platforms["y"],width=platforms["width"],height=platforms["heigth"],type=platforms["type"])
            self.platform_list.append(platform)

        return self.platform_list

    def get_walking_fideitos(self):
        fideitos_list_dic = self.data[self.nivel]["ground_enemy"]
        self.frutita_list = []

        for enemy in fideitos_list_dic:
            enemy_to_list = Enemy(x=enemy["x"],y=enemy["y"],r_limit=enemy["r_limit"],l_limit=enemy["l_limit"],speed_walk=enemy["speed_w"],speed_run=enemy["speed_r"],gravity=enemy["gravity"],frame_rate_ms=enemy["frame_rate_ms"],move_rate_ms=enemy["move_rate_ms"],dying_time=enemy["dying_t"],e_scale=enemy["e_scale"])
            self.frutita_list.append(enemy_to_list)

        return self.frutita_list

    def get_att_enemy(self):
        att_enemy_list_dic = self.data[self.nivel]["att_enemy"]
        self.frutita_list = []

        for enemy in att_enemy_list_dic:
            enemy_to_list = Attacking_Enemy(x=enemy["x"],y=enemy["y"],speed_walk=enemy["speed_walk"],speed_run=enemy["speed_run"],gravity=enemy["gravity"],frame_rate_ms=enemy["frame_rate_ms"],move_rate_ms=enemy["move_rate_ms"],dying_time=enemy["dying_time"],e_scale=enemy["e_scale"])
            self.frutita_list.append(enemy_to_list)

        return self.frutita_list

    def get_frutita(self):
        frutita_list_dic = self.data[self.nivel]["frutifrutona"]
        self.frutita_list = []

        for frutita in frutita_list_dic:
            frutita_to_list = Fruits(x=frutita["x"],y=frutita["y"],frame_rate_ms=frutita["frame_rate_ms"],move_rate_ms=frutita["move_rate_ms"],f_scale=frutita["f_scale"])
            self.frutita_list.append(frutita_to_list)

        return self.frutita_list

    @property
    def get_lvl_image(self):
        return self.__screen

    @property
    def get_player(self):
        return self.__player