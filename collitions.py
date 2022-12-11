import pygame
from constantes import *
from auxiliar import Auxiliar






class Collition():
    def __init__(self,enemy_list,player,att_enemy_list,fruit_list,fire_list,platform_list,key_list,door_list):
        self.att_enemy_list = att_enemy_list
        self.enemy_list = enemy_list
        self.player = player
        self.fruit_list = fruit_list
        self.fire_list = fire_list
        self.platform_list = platform_list
        self.key_list = key_list
        self.door_list = door_list
    def player_collide_enemy(self):
        
        if(self.enemy_list != None):
            for enemy in self.enemy_list: 

                if(self.player.ground_collition_rect.colliderect(enemy.head_collition_rect)):        
                    enemy.hit_on_head()
                    self.player.hit_on_enemy_or_fruit("ground_enemy")
                    return True
        if(self.att_enemy_list != None):
            for att_enemy in self.att_enemy_list: 

                if(self.player.ground_collition_rect.colliderect(att_enemy.head_collition_rect)):        
                    att_enemy.hit_on_head()
                    self.player.hit_on_enemy_or_fruit("att_enemy")
                    return True

    def player_pick_up_fruit(self):
        if(self.fruit_list != None):
            for frutitas in self.fruit_list:
                if(self.player.rect.colliderect(frutitas.rect)):
                    frutitas.pick_up_fruit()
                    self.player.hit_on_enemy_or_fruit(is_fruit = True)

    def player_collides_fire(self,fire_list):
        self.fire_list = fire_list
        if self.fire_list != None:
            for fire in self.fire_list:
                if(self.player.rect.colliderect(fire.rect)):
                    
                    fire.is_out_id(hit_player=True)
                    self.player.hit_by_enemy()
        
    def enemy_collide_player(self,delta_ms):
        if(self.enemy_list != None):
            for enemy in self.enemy_list:

                if(self.player.collition_rect.colliderect(enemy.enemy_collittion_rect)):
                    self.player.hit_by_enemy()
        if(self.att_enemy_list != None):
            for att_enemy in self.att_enemy_list:

                if(self.player.collition_rect.colliderect(att_enemy.enemy_collittion_rect)):
                    self.player.hit_by_enemy()

    def att_enemy_sees_player(self):
        if(self.att_enemy_list != None):
            for att_enemy in self.att_enemy_list:
                
                if(att_enemy.sight_range_rect_r.colliderect(self.player.collition_rect) or att_enemy.sight_range_rect_l.colliderect(self.player.collition_rect)):
                    #print("SAW PLAYER")
                    att_enemy.saw_player()
                    return True
    
    def player_hit_acid(self):
        for platform in self.platform_list:
            if(self.player.rect.colliderect(platform.acid_rect)):

                self.player.hit_by_enemy()
       
    def player_hit_spyke(self):

        for platform in self.platform_list:
            if(self.player.rect.colliderect(platform.spyke_rect)):

                self.player.hit_by_enemy()

    def player_gets_key(self):
        if(self.key_list != None):
            for keys in self.key_list:
                if(self.player.rect.colliderect(keys.rect)):
                    keys.pick_up_key()
                    self.player.grabs_key()
    
    def player_in_door(self):
        if(self.door_list != None):
            for door in self.door_list:
                if(self.player.rect.colliderect(door.rect)):

                    return True
                else: return False
