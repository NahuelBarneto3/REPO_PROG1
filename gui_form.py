#INGRESO DE DATOS
#NIVEL 3 MEZCLA DE LOS DOS ANTERIORES
#SQL

import pygame
from pygame.locals import *
from gui_widget import Widget
from gui_button import *
from auxiliar import Auxiliar
from constantes import *
from player import Player
from enemigo import Enemy
from plataforma import Plataform 
from collitions import Collition

from Enemy_fire import EnemyFire
from fruits import Fruits
from lvl_Config import LvlConfig
from sql import *

pygame.mixer.pre_init()
mixer.init()
#FORM DEL QUE HEREDO
class Form():
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,active,lvl):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y

        self.active = active
        self.surface = pygame.image.load("./assets/images/celeste-1.jpg").convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(ANCHO_VENTANA,ALTO_VENTANA))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.lvl = lvl
    #me activa el forms con el mismo nombre y desactiva los demas
    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            if aux_form.active:
                aux_form.active = False       
        self.forms_dict[name].active = True


    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)


class FormMenu(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)
        #self.main_menu_ttl =
        self.selected_lvl = lvl
        self.pushed_start = False
        self.puntajes_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2,text='Puntajes',screen=master_surface,on_click=self.click_puntajes,on_click_param="form_puntajes",font_size=40)
        self.option_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-200,text='Options',screen=master_surface,on_click=self.click_options,on_click_param="option_form",font_size=40)
        self.lvl_select_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-300,text='Seleccionar Nivel',screen=master_surface,on_click=self.click_select_lvl,on_click_param="form_lvl_select",font_size=40)
        # self.boton1 = Button(master=self,x=100,y=50,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="1234",text="MENU",font="Verdana",font_size=30,font_color=(0,255,0))
        # self.boton2 = Button(master=self,x=200,y=50,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="8",text="MENU 2",font="Verdana",font_size=30,font_color=(0,255,0))
        self.lista_widget = [self.option_btn,self.lvl_select_btn,self.puntajes_btn]#self.start_btn,
        
    def click_puntajes(self, parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
    def click_select_lvl(self, parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
    def click_options(self, parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
    # def click_start(self,parametro):
    #     self.set_active(parametro)
    #     click_sound.play(0,450,0)
    #     self.pushed_start = True

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()


class FormLvlStart(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)

        self.lvl = lvl
        
        self.screen = master_surface
        self.config = LvlConfig(self.lvl)
        self.in_door = False
        self.clock = pygame.time.Clock()
        # self.lvl_timer_min = self.config.get_timer_min()
        # self.lvl_last_timer_min = pygame.time.get_ticks()
        self.lvl_timer_sec = self.config.get_timer_sec()
        self.lvl_last_timer_sec = pygame.time.get_ticks()
        #al ser propiedad no lleva parentesis get_lvl_image
        self.imagen_fondo = pygame.image.load(self.config.get_lvl_image).convert_alpha()

        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        #ENEMIES
        self.ground_enemy_list = self.config.get_walking_fideitos()
        self.att_enemy_list = self.config.get_att_enemy()
        self.enemy_fire_list = self.config.get_enemy_fire()
        #OBJECTIVES
        self.fruits_list = self.config.get_frutita()
        self.key_list = self.config.get_keys()
        self.door_list = self.config.get_door()
        self.keys_needed = self.config.return_lvl_keys_needed
        
        #PLATFORMS
        self.platform_list = self.config.get_platforms()

        self.respawn_fire_list = []
        self.player_1 = self.config.get_player
        self.collition = Collition(self.ground_enemy_list,self.player_1,self.att_enemy_list,self.fruits_list,self.enemy_fire_list,self.platform_list,self.key_list,self.door_list)
        self.puntaje = self.player_1.get_player_score()


    # def config(self):
    #     self.config = LvlConfig(1)
    #     return self.config

    def update(self,keys):
        #UPDATES NECESARIOS DE LOS DIFERENTES OBJETOS
        self.delta_ms = self.clock.tick(FPS)
        for platform in self.platform_list:
            platform.update(self.delta_ms)
        if self.fruits_list!=None:
            for frutita in self.fruits_list:
                frutita.update(self.delta_ms)

        if self.key_list!=None:
            for key_element in self.key_list:
                key_element.update(self.delta_ms)
       
        if self.ground_enemy_list!=None:
            for enemy_element in self.ground_enemy_list:
                enemy_element.update(self.delta_ms,self.platform_list)

        if self.att_enemy_list!=None:
            for att_enemy_element in self.att_enemy_list:
                att_enemy_element.update(self.delta_ms,self.platform_list)

        #CHEQUEO QUE LAS TRAMPAS(BOLAS DE FUEGO LLEGUEN FUERA DE LA PANTALLA PARA PODER RESPAWNEARLAS)
        #print("FUEGO", len(self.enemy_fire_list))
        #if len(self.enemy_fire_list) > 0 and len(self.respawn_fire_list) != 3:    
        if self.enemy_fire_list != None:
            for enemy_fire_element in self.enemy_fire_list:               
                enemy_fire_element.update(self.delta_ms)
                if(enemy_fire_element.is_out_id() == 0 or enemy_fire_element.is_out_id() == 1 or enemy_fire_element.is_out_id() == 2):
                    self.enemy_fire_list = self.config.get_enemy_fire()
                    Collition(self.ground_enemy_list,self.player_1,self.att_enemy_list,self.fruits_list,self.enemy_fire_list,self.platform_list,self.key_list,self.door_list)
                #IDEA DE PASAR DE UNA LISTA A LA TRA UNA VEZ QUE SE FUERAN TODAS PARA QUE NO DESAPARECIERAN TODAS DE UNA 
                    #enemy_fire_element.is_out_id()
                # if(enemy_fire_element.is_out_id() == 0 or enemy_fire_element.is_out_id() == 1 or enemy_fire_element.is_out_id() == 2):
                #     self.respawn_fire_list = self.enemy_fire_list.pop(enemy_fire_element.is_out_id())
                #     enemy_fire_element.spawn_bullet()
            # else:
            #     for enemy_fire_element2 in self.respawn_fire_list:               
            #         enemy_fire_element2.update(self.delta_ms)
            #         if(enemy_fire_element.is_out_id() == 0 or enemy_fire_element.is_out_id() == 1 or enemy_fire_element.is_out_id() == 2):
            #             self.enemy_fire_list = self.respawn_fire_list.pop(enemy_fire_element.is_out_id())
            #             enemy_fire_element.spawn_bullet()
        
        #print(self.player_1.rect.y)
        #COLLITIONS, CHEQUEO TODAS LAS COLISIONES 
        self.collition.player_collide_enemy()
        self.collition.enemy_collide_player(self.delta_ms)
        self.collition.att_enemy_sees_player()
        self.collition.player_pick_up_fruit()
        #EL PROBLEMA QUE TENIA ES QUE EL ESPACIO DE MEMORIA CACMBIABA PORQUE ESTABA INSTANCIANDO LA LISTA CADA VEZ QUE UNA BALA SALIA, ESTA FUE LA SOLUCION
        self.collition.player_collides_fire(self.enemy_fire_list)#recibe cada vez el nuevo lugar de memoria en el que se esta alojando 
        self.collition.player_hit_acid()
        self.collition.player_gets_key()
        
        if(self.lvl_timer_sec > 0 ):
            timer_sec = pygame.time.get_ticks()
           # timer_min = pygame.time.get_ticks()
            if(timer_sec - self.lvl_last_timer_sec > ONE_SEC):
                self.lvl_last_timer_sec = timer_sec
                self.lvl_timer_sec -= 1
            #     if(self.lvl_last_timer_sec == 0 and self.lvl_last_timer_min != 0):
            #         self.lvl_last_timer_sec = 60
            # if(timer_min - self.lvl_last_timer_min > ONE_MIN):
            #     self.lvl_last_timer_min = timer_min
            #     self.lvl_last_timer_min -= 1


        if(self.player_1.get_player_keys() == self.keys_needed):
            self.in_door = self.collition.player_in_door()

        self.player_1.events(self.delta_ms,keys)
        self.player_1.update(self.delta_ms,self.platform_list)

        
        if(self.player_1.get_player_score() >= 2500 or self.in_door == True):
            self.win()

        # player_1.winning_state()
            if(self.ground_enemy_list != None):
                for ground_enemy in self.ground_enemy_list:
                    ground_enemy.winning_status()
            if(self.att_enemy_list != None):
                for att_enemy in self.att_enemy_list:
                    att_enemy.winning_status() 
            
        if self.player_1.get_player_lives() == 0 or self.lvl_timer_sec == 0:          
            if self.player_1.player_is_dead():
                death_sound.fadeout(5000)
                
                self.set_active("form_death")
                self.re_init()
        self.screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())
    def win(self):
        win_fanfare_sound.play()
        win_fanfare_sound.fadeout(10000)
        pygame.mixer.music.pause()
        self.score = self.player_1.get_player_score()
        self.lives = self.player_1.get_player_lives()
        self.time = self.lvl_timer_sec
        self.actual_lvl = self.lvl
        #self.set_active("form_name")
        # self.sql.add_puntuacion("NAHUEL",self.player_1.get_player_lives(),self.player_1.get_player_score(),self.lvl_timer_sec)


    def draw(self):
        
        for plataforma in self.platform_list:
            plataforma.draw(self.screen)
        if(self.fruits_list != None):
            for frutita in self.fruits_list:
                frutita.draw(self.screen)
        if(self.ground_enemy_list != None):
            for enemy_element in self.ground_enemy_list:
                enemy_element.draw(self.screen)
        if(self.att_enemy_list != None):
            for att_enemy_element in self.att_enemy_list:
                att_enemy_element.draw(self.screen)
        if(self.enemy_fire_list != None):
            for enemy_fire_element in self.enemy_fire_list:
                enemy_fire_element.draw(self.screen)
        if(self.key_list != None):
            for key_element in self.key_list:
                key_element.draw(self.screen)
        if(self.door_list != None):
            for door_element in self.door_list:
                door_element.draw(self.screen)
        self.player_1.draw(self.screen)

        time_sec_text_font = pygame.font.SysFont("segoe print",30)
        time_sec_text = time_sec_text_font.render("Time: "+str(self.lvl_timer_sec), True,(255,0,0))
        self.screen.blit(time_sec_text,(720,20))
       
        if(self.player_1.get_player_score() >= 2500 or self.in_door == True):


            self.set_active("form_name")
            self.player_1.reset()
            self.re_init()
        
    def re_init(self):

        self.config = LvlConfig(self.lvl)

        self.clock = pygame.time.Clock()

        #al ser propiedad no lleva parentesis get_lvl_image
        self.imagen_fondo = pygame.image.load(self.config.get_lvl_image).convert_alpha()

        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        #ENEMIGOS
        self.ground_enemy_list = self.config.get_walking_fideitos()
        self.att_enemy_list = self.config.get_att_enemy()
        #FRUTAS
        self.fruits_list = self.config.get_frutita()
        #PLAYER
        self.player_1 = self.config.get_player
        
        #PLATAFORMAS

        self.platform_list = self.config.get_platforms()
        self.enemy_fire_list = self.config.get_enemy_fire()

        self.collition = Collition(self.ground_enemy_list,self.player_1,self.att_enemy_list,self.fruits_list,self.enemy_fire_list,self.platform_list,self.key_list,self.door_list)




class FormOptions(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)

    #self.main_menu_ttl = 

        self.music_on_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-200,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
        self.music_off_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-100,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-300,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
        self.lista_widget = [self.music_off_btn,self.music_on_btn,self.back_btn]
        

    def click_music_on(self, parametro):
        pygame.mixer.music.unpause()
        click_sound.play(0,450,0)
    def click_music_off(self, parametro):
        pygame.mixer.music.pause()
        click_sound.play(0,450,0)
    def click_back(self,parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
    

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class FormPause(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)
  
    #self.main_menu_ttl = 
        self.lvl = lvl

        self.music_on_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-100,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
        self.music_off_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-200,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-300,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)

        self.resume_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2,text='Volver al juego',screen=master_surface,on_click=self.click_resume,on_click_param="form_start_lvl",font_size=40)
        self.lista_widget = [self.music_off_btn,self.music_on_btn,self.back_btn,self.resume_btn]

    
    
    def click_resume(self,parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
    def click_music_on(self, parametro):
        pygame.mixer.music.unpause()
        click_sound.play(0,450,0)
    def click_music_off(self, parametro):
        pygame.mixer.music.pause()
        click_sound.play(0,450,0)
    def click_back(self,parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
          

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class FormDeath(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)
        
        self.perdiste_txt = Texts(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-300,text='PERDISTE',screen=master_surface,font_size=70)
        self.music_on_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-100,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
        self.music_off_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-200,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-300,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
        self.perdiste_txt = Texts(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2+50,text='Perdiste',screen=master_surface,font_size=40)
        self.retry_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2+100,text='Reintentar',screen=master_surface,on_click=self.click_retry,on_click_param="menu_form",font_size=25)
                                                                                                                                                            #form_start_lvl
        self.lista_widget = [self.music_off_btn,self.music_on_btn,self.back_btn,self.retry_btn,self.perdiste_txt]

    def click_retry(self,parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
    def click_music_on(self, parametro):
        pygame.mixer.music.unpause()
        click_sound.play(0,450,0)
    def click_music_off(self, parametro):
        pygame.mixer.music.pause()
        click_sound.play(0,450,0)
    def click_back(self,parametro):
        self.set_active(parametro)
        pygame.mixer.music.unpause()


    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
    

class FormWin(Form):
    def __init__(self,name,master_surface,x,y,active,lvl,puntaje):
        super().__init__(name,master_surface,x,y,active,lvl)

        self.puntaje = puntaje
        self.music_on_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
        self.music_off_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-100,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-200,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
        self.ganaste_txt = Texts(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-300,text='Ganaste',screen=master_surface,font_size=70)
        self.puntaje_txt = Texts(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-400,text='Puntos {0}'.format(self.puntaje),screen=master_surface,font_size=50)
        
                                                                                                                                                     
        self.lista_widget = [self.puntaje_txt,self.music_off_btn,self.music_on_btn,self.back_btn,self.ganaste_txt]


    def click_music_on(self, parametro):
        pygame.mixer.music.unpause()

    def click_music_off(self, parametro):
        pygame.mixer.music.pause()

    def click_back(self,parametro):
        self.set_active(parametro)
        pygame.mixer.music.unpause()

        

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class FormLvlSelect(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)
        self.selected_lvl = lvl
        self.is_selected = False
        self.lvl1_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-300,text='Nivel 1',screen=master_surface,on_click=self.click_lvl1,on_click_param="form_start_lvl",font_size=40)
        self.lvl2_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-200,text='Nivel 2',screen=master_surface,on_click=self.click_lvl2,on_click_param="form_start_lvl",font_size=40)
        self.lvl3_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-100,text='Nivel 3',screen=master_surface,on_click=self.click_lvl3,on_click_param="form_start_lvl",font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2,text='Volver',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
                                                                                                                                                    
        self.lista_widget = [self.lvl1_btn,self.lvl2_btn,self.back_btn,self.lvl3_btn]
    
    
    def click_lvl1(self,parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
        self.selected_lvl = 1
        self.is_selected = True

    def click_lvl2(self, parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
        self.selected_lvl = 2
        self.is_selected = True
    def click_lvl3(self, parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
        self.selected_lvl = 3
        self.is_selected = True
    def click_back(self,parametro):
        self.set_active(parametro)
    

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class FormPuntuaciones(Form):
    def __init__(self,name,master_surface,x,y,active,lvl,ranks_db)->None:
        super().__init__(name,master_surface,x,y,active,lvl)

        self.show_ranks = []
        self.ranks_db=ranks_db

        self.puntuaciones_txt = Texts(x=ANCHO_VENTANA//2,y=ALTO_VENTANA//2-250,text="TOP 5 RANKINGS",screen=master_surface,font_size=50)
        self.back_btn = Button(x=ANCHO_VENTANA//2,y=ALTO_VENTANA//2+200,text="VOLVER AL MENU",screen=master_surface,on_click=self.click_back,on_click_param="menu_form")

        #if ranks_db != None :
        for i in range(len(ranks_db)):
            self.show_ranks.append(Texts(x=ANCHO_VENTANA//2-700,y=ALTO_VENTANA//2.5+i*25,text="{0}".format(i+1),screen=master_surface,font_size=25))
            self.show_ranks.append(Texts(x=ANCHO_VENTANA//2-450,y=ALTO_VENTANA//2.5+i*25,text="NOMBRE:{0}".format(ranks_db[i][1]),screen=master_surface,font_size=25))
            self.show_ranks.append(Texts(x=ANCHO_VENTANA//2-200,y=ALTO_VENTANA//2.5+i*25,text="VIDAS:{0}".format(ranks_db[i][2]),screen=master_surface,font_size=25))
            self.show_ranks.append(Texts(x=ANCHO_VENTANA//2+250,y=ALTO_VENTANA//2.5+i*25,text="PUNTAJE:{0}".format(ranks_db[i][3]),screen=master_surface,font_size=25))
            self.show_ranks.append(Texts(x=ANCHO_VENTANA//2+500,y=ALTO_VENTANA//2.5+i*25,text="TIEMPO:{0}".format(ranks_db[i][4]),screen=master_surface,font_size=25))
            self.show_ranks.append(Texts(x=ANCHO_VENTANA//2-50,y=ALTO_VENTANA//2.5+i*25,text="LVL:{0}".format(ranks_db[i][5]),screen=master_surface,font_size=25))

        print(self.show_ranks)
                 
        self.lista_widget = [self.puntuaciones_txt,self.back_btn]
    
    

    def click_back(self,parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        for ranks in self.show_ranks:
            ranks.draw()


class FormWin(Form):
    def __init__(self,name,master_surface,x,y,active,lvl,puntaje):
        super().__init__(name,master_surface,x,y,active,lvl)

        self.puntaje = puntaje
        self.music_on_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
        self.music_off_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-100,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-200,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
        self.ganaste_txt = Texts(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-300,text='Ganaste',screen=master_surface,font_size=70)
        self.puntaje_txt = Texts(x=ANCHO_VENTANA/2+300,y=ALTO_VENTANA//2-400,text='Puntos {0}'.format(self.puntaje),screen=master_surface,font_size=50)
        
                                                                                                                                                     
        self.lista_widget = [self.puntaje_txt,self.music_off_btn,self.music_on_btn,self.back_btn,self.ganaste_txt]


    def click_music_on(self, parametro):
        pygame.mixer.music.unpause()

    def click_music_off(self, parametro):
        pygame.mixer.music.pause()

    def click_back(self,parametro):
        self.set_active(parametro)
        pygame.mixer.music.unpause()

        

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class FormLvlSelect(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)
        self.selected_lvl = lvl
        self.is_selected = False
        self.lvl1_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-300,text='Nivel 1',screen=master_surface,on_click=self.click_lvl1,on_click_param="form_start_lvl",font_size=40)
        self.lvl2_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-200,text='Nivel 2',screen=master_surface,on_click=self.click_lvl2,on_click_param="form_start_lvl",font_size=40)
        self.lvl3_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-100,text='Nivel 3',screen=master_surface,on_click=self.click_lvl3,on_click_param="form_start_lvl",font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2,text='Volver',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
                                                                                                                                                    
        self.lista_widget = [self.lvl1_btn,self.lvl2_btn,self.back_btn,self.lvl3_btn]
    
    
    def click_lvl1(self,parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
        self.selected_lvl = 1
        self.is_selected = True

    def click_lvl2(self, parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
        self.selected_lvl = 2
        self.is_selected = True
    def click_lvl3(self, parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
        self.selected_lvl = 3
        self.is_selected = True
    def click_back(self,parametro):
        self.set_active(parametro)
    

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class FormName(Form):
    def __init__(self,name,master_surface,x,y,active,lvl)->None:
        super().__init__(name,master_surface,x,y,active,lvl)

        self.name_ok = False

        self.ingresar_nombre_txt = Texts(x=ANCHO_VENTANA//2,y=ALTO_VENTANA//2-450,text="INGRESAR NOMBRE",screen=master_surface,font_size=50)
        

        self.text_box = TextBox(x=ANCHO_VENTANA//2,y=ALTO_VENTANA//2+10,text="____________________",screen=master_surface,font_size=30)
        
        self.confirm_btn = Button(x=ANCHO_VENTANA//2,y=ALTO_VENTANA//2+350,text="CONFIRMAR NOMBRE",screen=master_surface,on_click=self.click_confirm,on_click_param="form_win")
        
                 
        self.lista_widget = [self.ingresar_nombre_txt,self.confirm_btn]
    
    

    def click_confirm(self,parametro):
        self.name_ok = True

    def update(self, lista_eventos):
        self.text_box.update(lista_eventos)
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        self.text_box.draw()
        self.writing_text = Texts(x=ANCHO_VENTANA//2,y=ALTO_VENTANA//2-20,text="{0}".format(self.text_box._writing.upper()),screen=self.master_surface,font_size=25)
        self.writing_text.draw()
        