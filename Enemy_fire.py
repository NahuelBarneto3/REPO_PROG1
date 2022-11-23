import pygame
from auxiliar import Auxiliar
from constantes import *

class EnemyFire:
    def __init__(self,bullet_speed,firing_cooldown,frame_rate_ms,b_scale):
        self.fire_anim_r = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Objects\Bullet_00{0}.png\\",5,flip=False, scale= b_scale)
        self.fire_anim_l = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Objects\Bullet_00{0}.png\\",5,flip=True, scale= b_scale)
        self.animation = self.fire_anim_r
        self.frame = 0
        self.image = self.animation[self.frame]
        self.tiempo_transcurrido_animation = 0
        self.animation = self.fire_anim_r
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 400

        self.frame_rate_ms = frame_rate_ms
        self.is_alive = True
        self.move_bullet_x = 0
        self.bullet_speed = bullet_speed
        self.firing_cooldown = firing_cooldown
        self.time_last_fired = 0

    def shoot(self):
        last_fire = pygame.time.get_ticks()
        if(last_fire - self.time_last_fired >= self.firing_cooldown):
            self.time_last_fired = last_fire
            self.change_fire_x(self.move_bullet_x)
            #if self.rect.x > self.rect.x:
            self.move_bullet_x = self.bullet_speed
            self.animation = self.fire_anim_r 
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

    def update(self,delta_ms):
        self.shoot()
        self.do_animation(delta_ms) 
        
    def draw(self,screen):
        if(self.is_alive == True):
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0,0),rect=self.rect)
                
                
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)