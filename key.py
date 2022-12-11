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
class Key:
    
    def __init__(self,x,y,frame_rate_ms,move_rate_ms,f_scale) -> None:
        self.key = Auxiliar.getSurfaceFromSeparateFiles(r"assets/elements/door_key_2/key.png",1,flip=False,scale=f_scale)
        self.image = self.key[0]
        self.move_y = 0
        self.speed_move = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame_rate_ms = frame_rate_ms

        self.winning_state = False
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms

        self.go_up = True
        self.contador = 0
        self.picked_up = False

        
    def change_y(self,delta_y):
        self.rect.y += delta_y
        
    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_y(self.move_y)
            if self.go_up:
                #print("ARRIBA",self.contador)
                self.move_y = -self.speed_move
                self.contador += 1
                if self.contador == 4:
                    self.go_up = False
            else:
                #print("ABAJO",self.contador)
                self.move_y = self.speed_move
                self.contador += 1 
                if self.contador == 8:
                    self.go_up = True
                    self.contador = 0


    def pick_up_key(self):
        self.rect = pygame.Rect(0,0,0,0)
        self.picked_up = True
       
    def update(self,delta_ms):
       self.do_animation(delta_ms)
       
    def draw(self,screen):
        if not self.picked_up:
            if not self.winning_state:
                if(DEBUG):
                    pygame.draw.rect(screen,color=(255,0,0),rect= self.rect)
               # print(self.rect)
                screen.blit(self.image,self.rect)