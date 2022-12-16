from enemigo import Enemy
import json
from constantes import *
from plataforma import Plataform
from enemigo import Enemy
from Attacking_Enemy import Attacking_Enemy
from fruits import Fruits
from player import Player
from Enemy_fire import EnemyFire
from key import Key
from exit_gate import Door

class LvlConfig():
    def __init__(self,lvl):
        self.lvl = lvl
        self.level_timer_sec = 0
        #self.level_timer_min = 0
        self.__keys_needed = 0
        match(self.lvl):
            case 1:
                self.data = self.CargarJson(path_lvl_1)
                self.level_timer_sec = 60
                #self.level_timer_min = 0
                self.nivel = "nivel_uno"
                self.__player = Player(x=10,y=463,respawn_pos_x=10,respawn_pos_y=600,speed_walk=8,speed_run=12,gravity=16,jump_power=40,frame_rate_ms=20,move_rate_ms=20,jump_height=150,p_scale=0.2,interval_time_jump=400)
                self.__screen = self.get_screen()
                self.tiles = self.get_tiles()
            case 2:
                self.data = self.CargarJson(path_lvl_2)
                self.level_timer_sec = 100
                #self.level_timer_min = 1
                self.__keys_needed = 1
                self.nivel = "nivel_dos"
                self.__player = Player(x=10,y=295,respawn_pos_x=10,respawn_pos_y=295,speed_walk=8,speed_run=12,gravity=16,jump_power=40,frame_rate_ms=20,move_rate_ms=20,jump_height=150,p_scale=0.2,interval_time_jump=400)
                self.__screen = self.get_screen()
                self.tiles = self.get_tiles()
            case 3:
                self.data = self.CargarJson(path_lvl_3)
                self.level_timer_sec = 100
                #self.level_timer_min = 1
                self.__keys_needed = 3
                self.nivel = "nivel_tres"
                self.__player = Player(x=650,y=150,respawn_pos_x=650,respawn_pos_y=150,speed_walk=8,speed_run=12,gravity=16,jump_power=40,frame_rate_ms=20,move_rate_ms=20,jump_height=150,p_scale=0.2,interval_time_jump=400)
                self.__screen = self.get_screen()
                self.tiles = self.get_tiles()



    def CargarJson(self,file):
        with open(file, 'r', encoding="utf-8") as f:
            self.data = json.load(f)
        return self.data
    
    def get_timer_sec(self):
        return self.level_timer_sec
    # def get_timer_min(self):
    #     return self.level_timer_min
                
    def get_screen(self):
        print(self.nivel)
        screen= self.data[self.nivel]["screen"]
        return screen

    def get_tiles(self):
        tiles= self.data[self.nivel]["tiles"]
        return tiles

    def get_door(self):
        exit_gate_list_dic = self.data[self.nivel]["exit_gate"]
        self.door_list = []
        
        if(len(exit_gate_list_dic) != 0):
            for door in exit_gate_list_dic:
                door_to_list = Door(x=door["x"],y=door["y"],frame_rate_ms=door["frame_rate_ms"],move_rate_ms=door["move_rate_ms"],d_scale=door["d_scale"])
                self.door_list.append(door_to_list)

            return self.door_list
    def get_keys(self):
        keys_list_dic = self.data[self.nivel]["keys"]
        self.keys_list = []
        
        if(len(keys_list_dic) != 0):
            for keys in keys_list_dic:
                keys_to_list = Key(x=keys["x"],y=keys["y"],frame_rate_ms=keys["frame_rate_ms"],move_rate_ms=keys["move_rate_ms"],f_scale=keys["f_scale"])
                self.keys_list.append(keys_to_list)

            return self.keys_list

    def get_platforms(self):
        
        platforms_list_dic = self.data[self.nivel]["platforms"]
        self.platform_list = []
        for platforms in platforms_list_dic:
            
            platform = Plataform(path=self.tiles,x=platforms["x"],y=platforms["y"],width=platforms["width"],height=platforms["heigth"],type=platforms["type"])
            self.platform_list.append(platform)

        return self.platform_list

    def get_walking_fideitos(self):
        fideitos_list_dic = self.data[self.nivel]["ground_enemy"]
        self.frutita_list = []
        if(len(fideitos_list_dic) != 0):
            for enemy in fideitos_list_dic:
                enemy_to_list = Enemy(x=enemy["x"],y=enemy["y"],r_limit=enemy["r_limit"],l_limit=enemy["l_limit"],speed_walk=enemy["speed_w"],speed_run=enemy["speed_r"],gravity=enemy["gravity"],frame_rate_ms=enemy["frame_rate_ms"],move_rate_ms=enemy["move_rate_ms"],dying_time=enemy["dying_t"],e_scale=enemy["e_scale"])
                self.frutita_list.append(enemy_to_list)

            return self.frutita_list

    def get_att_enemy(self):
        att_enemy_list_dic = self.data[self.nivel]["att_enemy"]
        self.frutita_list = []
        if(len(att_enemy_list_dic) != 0):
            for enemy in att_enemy_list_dic:
                enemy_to_list = Attacking_Enemy(x=enemy["x"],y=enemy["y"],speed_walk=enemy["speed_walk"],speed_run=enemy["speed_run"],gravity=enemy["gravity"],frame_rate_ms=enemy["frame_rate_ms"],move_rate_ms=enemy["move_rate_ms"],dying_time=enemy["dying_time"],e_scale=enemy["e_scale"])
                self.frutita_list.append(enemy_to_list)

            return self.frutita_list

    def get_frutita(self):
        frutita_list_dic = self.data[self.nivel]["frutifrutona"]
        self.frutita_list = []
        
        if(len(frutita_list_dic) != 0):
            for frutita in frutita_list_dic:
                frutita_to_list = Fruits(x=frutita["x"],y=frutita["y"],frame_rate_ms=frutita["frame_rate_ms"],move_rate_ms=frutita["move_rate_ms"],f_scale=frutita["f_scale"])
                self.frutita_list.append(frutita_to_list)

            return self.frutita_list

    def get_enemy_fire(self):
        enemy_fire_list_dic = self.data[self.nivel]["enemy_fire"]
        self.enemy_fire_list = []
        if(len(enemy_fire_list_dic) != 0):
            for fire in enemy_fire_list_dic:
                enemy_to_list = EnemyFire(id_b=fire["id_b"],bullet_speed=fire["bullet_speed"],firing_cd=fire["firing_cd"],frame_rate_ms=fire["fr_ms"],b_scale=fire["b_scale"])
                self.enemy_fire_list.append(enemy_to_list)

            return self.enemy_fire_list

    @property
    def get_lvl_image(self):
        return self.__screen

    @property
    def get_player(self):
        return self.__player

    @property
    def return_lvl_keys_needed(self):
        return self.__keys_needed