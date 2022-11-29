
from player import *
from constantes import *
from auxiliar import Auxiliar
from collitions import Collition
from Enemy_fire import EnemyFire
class Attacking_Enemy():
    def __init__(self,x,y,speed_walk,speed_run,gravity,frame_rate_ms,move_rate_ms,dying_time,e_scale=1) -> None:
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Run ({0}).png\\",8,flip=False,scale=e_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Run ({0}).png\\",8,flip=True,scale=e_scale)
        self.die_anim = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Dead ({0}).png\\",10,flip=False,scale=e_scale)
        self.stay = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Idle ({0}).png\\",10,flip=False,scale=e_scale)
        #self.sight_range = pygame.Rect()
        #self.fire_anim_r = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Objects\Bullet_00{0}.png\\",5,flip=False, scale= e_scale)
        #self.fire_anim_l = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\robot\Objects\Bullet_00{0}.png\\",5,flip=True, scale= e_scale)
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.dying_time = dying_time
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contador_player = 0
        self.collide = False
        self.is_alive = True
        self.tiempo_ultimo_pos = 0
        self.contador = 0
        self.tiempo_transcurrido_animation = 0 
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido_move = 0

        self.count_time_col = 0
        self.is_alive = True
        self.head_collition_rect= pygame.Rect(self.rect.x + self.rect.w / 4.5, self.rect.y-5,self.rect.w/1.8,self.rect.h/5)
        self.ground_collition_rect = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_COLLIDE_H, self.rect.w / 3, GROUND_COLLIDE_H)
        self.enemy_collittion_rect = pygame.Rect(self.rect.x + self.rect.w / 4.2,self.rect.y+20,self.rect.w/1.8,self.rect.h/1.5)
        self.sight_range_rect_r= pygame.Rect(self.rect.x + self.rect.w,self.rect.y/0.7,self.rect.w*2,self.rect.h/2)
        self.sight_range_rect_l= pygame.Rect(self.rect.x - self.rect.w/0.5,self.rect.y/0.7,self.rect.w/0.5,self.rect.h/2)

        self.winnin_state = False

        
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.head_collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.enemy_collittion_rect.x += delta_x
        self.sight_range_rect_r.x += delta_x
        self.sight_range_rect_l.x += delta_x
    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.head_collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.enemy_collittion_rect.y += delta_y
        self.sight_range_rect_r.y += delta_y
        self.sight_range_rect_l.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.collide == False):
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0
                self.change_x(self.move_x)
                #print(self.rect.x)
                if self.contador <= 300 and self.rect.x >= 548:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1 
                elif self.contador <= 500:
                    self.move_x = 0
                    self.animation = self.stay
                    self.contador += 1
                elif self.contador <= 800 and self.rect.x <= 849:                      
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                elif self.contador <= 1000:
                    self.move_x = 0
                    self.animation = self.stay
                    self.contador += 1
                else:
                    self.contador = 0
        '''
        if self.go_left == True and self.contador == 0:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    if self.rect.x == 549:
                        self.go_left = False
                        self.do_stay = True
                        self.contador = 1
                elif self.do_stay == True and self.contador <= 50:
                    self.move_x = 0
                    self.animation = self.stay
                    self.contador += 1
                    print(self.contador)
                    if self.contador == 50:
                        self.do_stay = False
                elif self.go_left == False and self.contador == 50:                      
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    if self.rect.x == 850:
                        
                        self.go_left = True
                        self.do_stay = True
                        self.contador = 51
                        print("LEFT")
                else: #self.contador <= 51 and self.do_stay == True:
                    self.move_x = 0
                    self.animation = self.stay
                    self.contador += 1
                    print("STAY")
                    print(self.contador)
                    if self.contador == 100:
                        self.go_left = True
                        self.contador = 0
        '''
        
        '''              
    def hit_on_enemy(self,enemy_type):   
        last_score = pygame.time.get_ticks()
        if(last_score - self.time_last_score >= self.score_cooldown):
            if(enemy_type == "att_enemy"):
                self.player_score += 1500
                self.time_last_score = last_score
            else:
                self.player_score += 500
                self.time_last_score = last_score
        '''
    def saw_player(self):       
        if(self.collide == False):           
                self.change_x(self.move_x)
                #print(self.rect.x)
                if self.contador_player <= 50:
                    self.move_x = -self.speed_walk - 9
                    self.animation = self.walk_l
                    self.contador_player += 1 
                    #print("CONTADOR PLAYER",self.contador_player)
                    if self.rect.x <= 548:
                        self.contador_player = 51
                elif self.contador_player <= 100:                 
                    self.move_x = self.speed_walk + 9
                    self.animation = self.walk_r
                    self.contador_player += 1
                    if self.rect.x >= 849:
                        self.contador_player = 0
                else:
                    self.contador_player = 0
                    
    def winning_status(self):
        self.winnin_state = True

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
            # elif (self.frame >= (len(self.animation) - 1)):
            #     self.frame = 0      
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
   

    def update(self,delta_ms,plataform_list):
            self.do_movement(delta_ms,plataform_list)
            self.do_animation(delta_ms) 
            

    def draw(self,screen):
        if(not self.winnin_state):
            if(self.is_alive == True):
                if(DEBUG):
                    pygame.draw.rect(screen,color=(0,0,255),rect=self.enemy_collittion_rect)
                    pygame.draw.rect(screen,color=(255,0 ,0),rect=self.head_collition_rect)
                    pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
                    pygame.draw.rect(screen,color=(0,0,255),rect=self.sight_range_rect_r)
                    pygame.draw.rect(screen,color=(0,0,255),rect=self.sight_range_rect_l)
                try:
                    self.image = self.animation[self.frame]
                except IndexError:
                    print("ATTERROR",self.frame,len(self.animation))
                screen.blit(self.image,self.rect)
