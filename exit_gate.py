from player import *
from constantes import *
from auxiliar import Auxiliar
from collitions import Collition
import pygame



'''
   surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
'''
class Door:
    
    def __init__(self,x,y,frame_rate_ms,move_rate_ms,d_scale) -> None:
        self.door = Auxiliar.getSurfaceFromSpriteSheet(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\elements\anti_gravitys_rainbow\puerta.png\\",6,8,flip=False,scale=d_scale)
        self.animation = self.door
        self.frame = 0
        self.image = self.animation[self.frame]
        self.move_y = 0
        self.speed_move = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_animation = 0
        self.winning_state = False
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms


        self.picked_up = False

        
    def change_y(self,delta_y):
        self.rect.y += delta_y
        
    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0


    def door_open(self):
        self.open = True
        return True
       
    def update(self,delta_ms):

        self.do_animation(delta_ms)
       
    def draw(self,screen):
        if not self.picked_up:
            if not self.winning_state:
                if(DEBUG):
                    pygame.draw.rect(screen,color=(255,0,0),rect= self.rect)
               # print(self.rect)
                screen.blit(self.image,self.rect)