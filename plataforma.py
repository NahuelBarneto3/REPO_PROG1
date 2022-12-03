import pygame
from constantes import *
from auxiliar import Auxiliar



class Plataform:
    def __init__(self,path, x, y,width, height,  type=1,move_rate_ms=60):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(path+r"\{0}.png\\",18,flip=False,w=width,h=height)
        self.type = type
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        

        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

        self.tiempo_transcurrido_move = 0
        self.speed_move = 1
        self.move_rate_ms = move_rate_ms
        self.go_up = True
        if self.type == 16 or self.type == 17:
            self.ground_collition_rect = pygame.Rect(0,0,0,0)
            self.acid_rect = pygame.Rect(self.rect)
            
            


    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            if self.type == 16 or self.type == 17:
                pygame.draw.rect(screen,color=(0,0,255),rect=self.acid_rect)
        #queda para despues las animaciones


    def do_animation(self,delta_ms):
        if type == 16 or type == 17:
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