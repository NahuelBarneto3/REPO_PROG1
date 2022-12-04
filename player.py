import pygame
from constantes import *
from auxiliar import Auxiliar
from enemigo import Enemy
from collitions import Collition


class Player:
    def __init__(self,x,y,respawn_pos_x,respawn_pos_y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''
        
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Idle ({0}).png\\",10,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Idle ({0}).png\\",10,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Jump ({0}).png\\",10,flip=False,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Jump ({0}).png\\",10,flip=True,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Run ({0}).png\\",8,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Run ({0}).png\\",8,flip=True,scale=p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Shoot ({0}).png\\",3,flip=False,scale=p_scale,repeat_frame=2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Shoot ({0}).png\\",3,flip=True,scale=p_scale,repeat_frame=2)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Melee ({0}).png\\",7,flip=False,scale=p_scale,repeat_frame=1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Melee ({0}).png\\",7,flip=True,scale=p_scale,repeat_frame=1)
        self.hit = Auxiliar.getSurfaceFromSeparateFiles(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\caracters\players\cowgirl\Dead ({0}).png\\",4,flip=False,scale=p_scale,repeat_frame=1)
        self.frame = 0
        self.respawn_pos_x = respawn_pos_x
        self.respawn_pos_y = respawn_pos_y
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/4,y,self.rect.width/2.5,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

        self.player_score = 0
        self.score_text = 0
        self.hit_flag = 0

        self.score_cooldown = 4000
        self.lives = 5
        self.invulnerability_timer = 2000
        self.count_time_col  = 0
        self.time_last_hit = pygame.time.get_ticks()
        self.time_last_score = pygame.time.get_ticks()
        
        self.player_dead = False
        self.winning_state = False

    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction
            if(direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                
                    
    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l       

    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l      

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            if(self.rect.x > -23 and self.rect.x < 1410):
                #print(self.rect.x)
                self.change_x(self.move_x)
            elif(self.rect.x <= -23):
                self.change_x(1)
            elif self.rect.x >= 1410:
                self.change_x(-1)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False            

    def is_on_plataform(self,plataform_list):
        retorno = False

        if self.player_dead == False:
            if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
                retorno = True     
            else:
                for plataforma in  plataform_list:
                    if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect) and plataforma.type != 14):
                        retorno = True
                        #print("a")
                        break
                    elif(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)) and plataforma.type == 14:     
                        #print("b")
                        retorno = True
                        self.change_y(plataforma.return_y())
            return retorno  
        else: return False               

    def hit_on_enemy_or_fruit(self,enemy_type="ground_enemy",is_fruit=False):   
        last_score = pygame.time.get_ticks()
        if(is_fruit == False):
            if(last_score - self.time_last_score >= self.score_cooldown):
                if(enemy_type == "att_enemy"):
                    self.player_score += 1
                    self.time_last_score = last_score
                else:
                    self.player_score += 500
                    self.time_last_score = last_score
        else:
            self.player_score += 200

    def get_player_score(self):
        return self.player_score

    def draw_player_won(self):
        self.winning_state = True
    
    def reset(self):
        self.rect.x = self.respawn_pos_x
        self.rect.y = self.respawn_pos_y
        self.collition_rect.x = self.respawn_pos_x+30
        self.ground_collition_rect.x = self.respawn_pos_x+30
        self.collition_rect.y = self.respawn_pos_y
        self.ground_collition_rect.y = self.respawn_pos_y+99
        self.lives = 5
        self.score = 0


    def do_respawn(self):
        self.rect.x = self.respawn_pos_x
        self.rect.y = self.respawn_pos_y
        self.collition_rect.x = self.respawn_pos_x+30
        self.ground_collition_rect.x = self.respawn_pos_x+30
        self.collition_rect.y = self.respawn_pos_y
        self.ground_collition_rect.y = self.respawn_pos_y+99
    
    def hit_by_enemy(self):
        self.do_respawn()
        last_hit =pygame.time.get_ticks()
        if(last_hit - self.time_last_hit >= self.invulnerability_timer):
            
            self.time_last_hit = last_hit
            self.lives -= 1
            #mover playar para atras

            #self.

    def draw_lives(self):
        lives_font = pygame.font.SysFont("segoe print",30)
        lives_text = lives_font.render("Lives: "+str(self.lives), True,(255,0,0))
        return lives_text

    def draw_score(self):
        score_text_font = pygame.font.SysFont("segoe print",30)
        score_text = score_text_font.render("Score: "+str(self.player_score), True,(255,0,0))
        return score_text
    
    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0
    
    def get_player_lives(self):
        return self.lives

    def player_is_dead(self):
        self.player_dead = True
        return self.player_dead
    # def winning_state(self):
    #     self.speed_walk = 0
    #     self.winning_state = True

    def update(self,delta_ms,plataform_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        
    
    def draw(self,screen):
        if(self.player_dead == False):
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
                pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            lives_in_screen = self.draw_lives()
            score_in_screen = self.draw_score()
            self.image = self.animation[self.frame]
            screen.blit(score_in_screen,(10,10))
            screen.blit(lives_in_screen,(10,50))
            screen.blit(self.image,self.rect)
        

    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms

        if(not self.winning_state):
            if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
                self.walk(DIRECTION_L)

            if(keys[pygame.MOUSEBUTTONDOWN]):
                self.mouse()

            if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                self.walk(DIRECTION_R)

            if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                self.stay()
            if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                self.stay()  

            if(keys[pygame.K_SPACE]):
                if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                    self.jump(True)
                    self.tiempo_last_jump = self.tiempo_transcurrido

            if(not keys[pygame.K_a]):
                self.shoot(False)  

            if(not keys[pygame.K_a]):
                self.knife(False)  

            if(keys[pygame.K_s] and not keys[pygame.K_a]):
                self.shoot()   
            
            if(keys[pygame.K_a] and not keys[pygame.K_s]):
                self.knife()   
            
          
