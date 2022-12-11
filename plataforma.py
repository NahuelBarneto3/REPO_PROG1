import pygame
from constantes import *
from auxiliar import Auxiliar
import random



class Plataform:
    def __init__(self,path, x, y,width, height,  type=1,move_rate_ms=20, change_direction= True):
        self.path = path
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(path+r"\{0}.png\\",23,flip=False,w=width,h=height)
        self.type = type
        #self.move = move podria haber hecho un self move y que si estuviera trrue mover la plataforma y si no no, pero ya tenia demasiadas plataformas
        #hechas de esta manera por lo que cambiarlo me llevaba demasiado cambio y asi cada nivel puede tener mejor distruibuidas las plataformas
        #y es mas facil de modificar, al miismo tiempo simp[lificaria] mucho codigo
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.move_x = 0
        self.move_y = 0
        self.delta_x = 0
        self.delta_y = 0
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.spyke_rect = pygame.Rect(0,0,0,0)
        self.acid_rect = pygame.Rect(0,0,0,0)
        self.wall_rect = pygame.Rect(0,0,0,0)
        self.tiempo_transcurrido_move = 0
        self.speed_move = 1
        self.move_rate_ms = move_rate_ms
        self.change_direction = change_direction
        self.contador = 0

        if self.type == ACID_TOP or self.type == ACID_BOTTOM:
            self.collition_rect = pygame.Rect(0,0,0,0)
            self.ground_collition_rect = pygame.Rect(0,0,0,0)
            self.acid_rect = pygame.Rect(self.rect)
        if self.type == SPYKE or self.type == 18:
            self.collition_rect = pygame.Rect(0,0,0,0)
            self.ground_collition_rect = pygame.Rect(0,0,0,0)
            self.spyke_rect = pygame.Rect(0,0,0,0)
        if self.type == WALL_FACING_L:
            self.ground_collition_rect = pygame.Rect(0,0,0,0)
            self.wall_rect = pygame.Rect(x+self.rect.w/8,y,self.rect.w/4,self.rect.h)

    def do_animation(self,delta_ms):
        if self.path != "./assets/tileset/forest/Tiles":
            self.tiempo_transcurrido_move += delta_ms
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0
                if self.type == ACID_TOP or self.type == ACID_BOTTOM:
                        self.change_y(self.move_y)
                        if self.change_direction:
                            #print("ARRIBA",self.contador)
                            self.move_y = -self.speed_move
                            self.contador += 1
                            if self.contador == 10:
                                self.change_direction = False
                        else:
                            #print("ABAJO",self.contador)
                            self.move_y = self.speed_move
                            self.contador += 1 
                            if self.contador == 20:
                                self.change_direction = True
                                self.contador = 0
                if self.type == MOVING_Y_PLATFORM or self.type == SPYKE:
                    self.change_y(self.move_y)
                    if self.change_direction:
                        #print("ARRIBA",self.contador)
                        self.move_y = (-self.speed_move)
                        self.contador += 1
                        if self.contador == 50:
                            self.change_direction = False
                    else:
                        #print("ABAJO",self.contador)
                        self.move_y = self.speed_move
                        self.contador += 1 
                        if self.contador == 100:
                            self.change_direction = True
                            self.contador = 0
                if self.type == MOVING_X_PLATFORM:
                    self.change_x(self.move_x)
                    if self.change_direction:
                        #print("ARRIBA",self.contador)
                        self.move_x = (-self.speed_move)
                        self.contador += 1
                        if self.contador == 100:
                            self.change_direction = False
                    else:
                        #print("ABAJO",self.contador)
                        self.move_x = self.speed_move
                        self.contador += 1 
                        if self.contador == 200:
                            self.change_direction = True
                            self.contador = 0
                            
    def change_x(self,delta_x):
        if self.type == MOVING_X_PLATFORM:
            self.ground_collition_rect.x += delta_x
            self.collition_rect.x += delta_x
            self.delta_x = delta_x
            self.return_x()

        elif self.type == SPYKE:
            self.spyke_rect.x += delta_x
            self.collition_rect.x += delta_x
        self.rect.x += delta_x
        
    def return_x(self): #envia cuanto esta moviendo la plataforma para enviarselo al player
        return self.delta_x

    def change_y(self,delta_y):
        if self.type == MOVING_Y_PLATFORM:
            self.ground_collition_rect.y += delta_y
            self.collition_rect.y += delta_y
            self.delta_y = delta_y
            self.return_y()
        elif self.type == SPYKE:
            self.spyke_rect.y += delta_y
            self.collition_rect.y += delta_y
        self.rect.y += delta_y
    def return_y(self): #envia cuanto esta moviendo la plataforma para enviarselo al player
        return self.delta_y

    def update(self,delta_ms):
        self.do_animation(delta_ms)

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            if self.type == ACID_TOP or self.type == ACID_BOTTOM:
                pygame.draw.rect(screen,color=(0,0,255),rect=self.acid_rect)
            elif self.type == SPYKE or self.type == 18:
                pygame.draw.rect(screen,color=(0,0,255),rect=self.spyke_rect)
            elif self.type == WALL_FACING_L:
                pygame.draw.rect(screen,color=(255,0,255),rect=self.wall_rect)
        #queda para despues las animaciones