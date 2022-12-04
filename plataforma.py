import pygame
from constantes import *
from auxiliar import Auxiliar
import random


class Plataform:
    def __init__(self,path, x, y,width, height,  type=1,move_rate_ms=20, go_up= True):
        self.path = path
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(path+r"\{0}.png\\",18,flip=False,w=width,h=height)
        self.type = type
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.move_y = 0
        self.delta_y = 0
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.spyke_rect = pygame.Rect(0,0,0,0)
        self.tiempo_transcurrido_move = 0
        self.speed_move = 1
        self.move_rate_ms = move_rate_ms
        self.go_up = go_up
        self.contador = 0

        if self.type == 16 or self.type == 17:
            self.ground_collition_rect = pygame.Rect(0,0,0,0)
            self.acid_rect = pygame.Rect(self.rect)
        if self.type == 15:
            self.ground_collition_rect = pygame.Rect(0,0,0,0)
            self.spyke_rect = pygame.Rect(x+self.rect.w/4,y+self.rect.h/2,self.rect.w/2,self.rect.h/2)


    def do_animation(self,delta_ms):
        if self.path != r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\tileset\forest\Tiles":
            self.tiempo_transcurrido_move += delta_ms
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0
                if self.type == 16 or self.type == 17:
                        self.change_y(self.move_y)
                        if self.go_up:
                            #print("ARRIBA",self.contador)
                            self.move_y = -self.speed_move
                            self.contador += 1
                            if self.contador == 10:
                                self.go_up = False
                        else:
                            #print("ABAJO",self.contador)
                            self.move_y = self.speed_move
                            self.contador += 1 
                            if self.contador == 20:
                                self.go_up = True
                                self.contador = 0
                if self.type == 14 or self.type == 15:
                    self.change_y(self.move_y)
                    if self.go_up:
                        #print("ARRIBA",self.contador)
                        self.move_y = (-self.speed_move)/2
                        self.contador += 1
                        if self.contador == 50:
                            self.go_up = False
                    else:
                        #print("ABAJO",self.contador)
                        self.move_y = self.speed_move
                        self.contador += 1 
                        if self.contador == 100:
                            self.go_up = True
                            self.contador = 0

    
    def change_y(self,delta_y):
        if self.type == 14:
            self.ground_collition_rect.y += delta_y
            self.collition_rect.y += delta_y
            self.delta_y = delta_y
            self.return_y()
        elif self.type == 15:
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
            if self.type == 16 or self.type == 17:
                pygame.draw.rect(screen,color=(0,0,255),rect=self.acid_rect)
            elif self.type == 15:
                pygame.draw.rect(screen,color=(0,0,255),rect=self.spyke_rect)

        #queda para despues las animaciones