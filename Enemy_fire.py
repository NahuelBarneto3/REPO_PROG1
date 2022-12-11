import pygame
from auxiliar import Auxiliar
from constantes import *
import random
class EnemyFire:
    
    def __init__(self,id_b,bullet_speed,firing_cd,frame_rate_ms,b_scale):
        self.fire_anim_r = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Objects\Bullet_00{0}.png\\",5,flip=False, scale= b_scale)
        self.fire_anim_l = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Objects\Bullet_00{0}.png\\",5,flip=True, scale= b_scale)
        self.id = id_b
        self.animation = self.fire_anim_r
        self.direction = random.randrange(0,2)
        self.frame = 0
        self.image = self.animation[self.frame]
        self.tiempo_transcurrido_animation = 0
        self.animation = self.fire_anim_r
        self.rect = self.image.get_rect()
        self.rect.x = self.spawn_direction()
        self.rect.y = random.randrange(0,BULL_SPAWN_Y)
        self.frame_rate_ms = frame_rate_ms
        self.is_alive = True
        self.move_bullet_x = 0
        self.bullet_speed = bullet_speed
        self.time_last_fired = 0
        self.firing_cd = firing_cd


    def spawn_direction(self):
        #print("DIREC",self.direction)
        if self.direction == DIRECTION_L: #L = 0
            return OUT_SCREEN_R
        else: return OUT_SCREEN_L
            

    def spawn_bullet(self):
            self.direction = random.randrange(0,2) #desde el 0 hasta el valor dado sin contarlo
            self.rect.y = random.randrange(10,BULL_SPAWN_Y,20)
            self.rect.x = self.spawn_direction()

    def shoot(self):
        last_fire = pygame.time.get_ticks()
        if(last_fire - self.time_last_fired >= self.firing_cd):
            self.time_last_fired = last_fire
            self.change_fire_x(self.move_bullet_x)
            #if self.rect.x > self.rect.x:
            if(self.direction == 1):
                self.move_bullet_x = self.bullet_speed
                self.animation = self.fire_anim_r
            else:
                self.move_bullet_x = -self.bullet_speed
                self.animation = self.fire_anim_l
            # else:
            #     self.move_bullet_x = -self.bullet_speed
            #     self.animation = self.fire_anim_l 
    
    def change_fire_x(self,delta_bullet_x):
        self.rect.x += delta_bullet_x
       # self.sight_range_l += delta_x

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0
    
    def is_out_id(self,hit_player=False): #tambien lo uso para si pega contra el player
        if(self.rect.x < OUT_SCREEN_L or self.rect.x > OUT_SCREEN_R or hit_player == True):
            return self.id
     
    
    def update(self,delta_ms):
        self.shoot()
        self.do_animation(delta_ms) 
        self.time_last_fired = delta_ms
        if(self.time_last_fired > self.firing_cd):
            self.time_last_fired = 0
            self.spawn_bullet()
        
    def draw(self,screen):
        if(self.is_alive == True):
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0,0),rect=self.rect)
                
                
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)