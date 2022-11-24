import pygame
from constantes import *
from auxiliar import Auxiliar





class Collition():
    def __init__(self,enemy_list,player,att_enemy_list,fruit_list):
        self.att_enemy_list = att_enemy_list
        self.enemy_list = enemy_list
        self.player = player
        self.fruit_list = fruit_list

    def player_collide_enemy(self):

        for enemy in self.enemy_list: 

            if(self.player.ground_collition_rect.colliderect(enemy.head_collition_rect)):        
                enemy.hit_on_head()
                self.player.hit_on_enemy_or_fruit("ground_enemy")
                return True
    
        for att_enemy in self.att_enemy_list: 

            if(self.player.ground_collition_rect.colliderect(att_enemy.head_collition_rect)):        
                att_enemy.hit_on_head()
                self.player.hit_on_enemy_or_fruit("att_enemy")
                return True

    def player_pick_up_fruit(self):
        for frutitas in self.fruit_list:
            if(self.player.rect.colliderect(frutitas.rect)):
                frutitas.pick_up_fruit()
                self.player.hit_on_enemy_or_fruit(is_fruit = True)

    def enemy_collide_player(self,delta_ms):
        for enemy in self.enemy_list:

            if(self.player.collition_rect.colliderect(enemy.enemy_collittion_rect)):
                self.player.hit_by_enemy()

        for att_enemy in self.att_enemy_list:

            if(self.player.collition_rect.colliderect(att_enemy.enemy_collittion_rect)):
                self.player.hit_by_enemy()

    def att_enemy_sees_player(self):
        for att_enemy in self.att_enemy_list:
            
            if(att_enemy.sight_range_rect_r.colliderect(self.player.collition_rect) or att_enemy.sight_range_rect_l.colliderect(self.player.collition_rect)):
                #print("SAW PLAYER")
                att_enemy.saw_player()
                return True
                
                
