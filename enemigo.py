from player import *
from constantes import *
from auxiliar import Auxiliar
from collitions import Collition
import random
class Enemy:
    
    def __init__(self,x,y,r_limit,l_limit,speed_walk,speed_run,gravity,frame_rate_ms,move_rate_ms,dying_time,e_scale) -> None:
        
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\jueguito\images\inhabitants\dust\walk_right.png\\",9,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\jueguito\images\inhabitants\dust\walk_left.png\\",8,1)
        self.die_anim = Auxiliar.getSurfaceFromSpriteSheet(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\effects\explosions\explosion-3.png\\",10,1)
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.animation = self.walk_r
        self.image = self.animation[self.frame]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.right_limit = r_limit
        self.left_limit = l_limit
        self.turn = False

        self.tiempo_ultimo_pos = 0
        self.contador = 0
        self.tiempo_transcurrido_animation = 0 
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido_move = 0

        self.is_alive = True
        self.head_collition_rect= pygame.Rect(self.rect.x + self.rect.w / 4.5, self.rect.y-5,self.rect.w/1.8,self.rect.h/5)
        self.ground_collition_rect = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_COLLIDE_H, self.rect.w / 3, GROUND_COLLIDE_H)
        self.enemy_collittion_rect = pygame.Rect(self.rect.x + self.rect.w / 4.2,self.rect.y+20,self.rect.w/1.8,self.rect.h/1.5)

        self.random_move_l = random.randrange(2,5)
        self.random_move_r = random.randrange(7,10)

        self.time_last_col = 0
        self.dying_time = dying_time
        self.collide = False
        self.count_time_col = 0
        self.tiempo_delay = 0
        self.winning_state = False

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.head_collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.enemy_collittion_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.head_collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.enemy_collittion_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.collide == False):
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0 
                if(self.tiempo_delay <= 100):
                    self.tiempo_delay += 1
                else:
                    self.random_move_l = random.randrange(2,5)
                    self.random_move_r = random.randrange(7,10)
                    #print(self.random_move_l)
                    #print(self.random_move_r)
                    self.tiempo_delay = 0
                self.change_x(self.move_x)                   
                #print("C",self.contador)
                if self.turn == False:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1
                    #print(self.rect.x)
                    
                    if ((self.rect.x <= self.left_limit) or (self.contador == (self.random_move_l*10))):
                        #print("LLIMIT",self.left_limit)
                        self.turn = True
                       # print("L")
                else:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                   #print(self.rect.x)
                    
                    if ((self.rect.x >= self.right_limit) or (self.contador == (self.random_move_r*10))):
                       # print("RLIMIT",self.right_limit)
                        self.turn = False
                        self.contador = 0
                        #print("R")

    def hit_on_head(self):
        
        if(self.is_alive == True):
                
            self.frame = 0
            self.animation = self.die_anim
            self.speed_walk =  0
            self.speed_run =  0
            self.time_last_col = pygame.time.get_ticks()  
            self.enemy_collittion_rect = pygame.Rect(0,0,0,0)     
            self.collide = True

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.collide == False):
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                    #print(self.frame)
                else: 
                    self.frame = 0
        else:
            self.time_last_col = delta_ms
            if(self.time_last_col >= self.dying_time):
                self.time_last_col = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 0 
                    #print(self.frame)
                    self.count_time_col += 1
                    if(self.animation[-1] and self.count_time_col == 100):
                        self.is_alive = False
                        self.rect = pygame.Rect(0,0,0,0)
                        self.head_collition_rect = pygame.Rect(0,0,0,0)
                        self.enemy_collittion_rect = pygame.Rect(0,0,0,0)
                        self.ground_collition_rect = pygame.Rect(0,0,0,0)
                else: 
                    self.frame = 0
                
    '''
       def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno    
    '''
    
    def winning_status(self):
        
        self.winning_state = True
        print(type(self.winning_state))
        

    def update(self,delta_ms,plataform_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms) 

    def draw(self,screen):
        if(not self.winning_state):
            if(self.is_alive == True):
                if(DEBUG):
                    pygame.draw.rect(screen,color=(0,0,255),rect=self.enemy_collittion_rect)
                    pygame.draw.rect(screen,color=(255,0 ,0),rect=self.head_collition_rect)
                    pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
                try:
                    self.image = self.animation[self.frame]
                except IndexError:
                    print("ATTERROR",self.frame,len(self.animation))
                screen.blit(self.image,self.rect)
