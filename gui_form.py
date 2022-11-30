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

pygame.mixer.pre_init()
mixer.init()

class Form():
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,active,lvl):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y

        self.active = active
        self.surface = pygame.image.load(r'D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\images\celeste-1.jpg').convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(ANCHO_VENTANA,ALTO_VENTANA))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.lvl = lvl
    #me activa el forms con el mismo nombre y desactiva los demas
    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    # def render(self):
    #     pass

    # def update(self,lista_eventos):
    #     pass

    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)


class FormMenu(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)
        #self.main_menu_ttl =

        
        self.start_btn = Button(x=ANCHO_VENTANA/1.2,y=ALTO_VENTANA//2-100,text='start',screen=master_surface,on_click=self.click_start,on_click_param="form_start_lvl",font_size=40)
        self.option_btn = Button(x=ANCHO_VENTANA/1.2,y=ALTO_VENTANA//2-200,text='options',screen=master_surface,on_click=self.click_start,on_click_param="option_form",font_size=40)
        self.lvl_select_btn = Button(x=ANCHO_VENTANA/1.2,y=ALTO_VENTANA//2-300,text='Seleccionar\n   Nivel',screen=master_surface,on_click=self.click_select_lvl,on_click_param="form_lvl_select",font_size=40)
        # self.boton1 = Button(master=self,x=100,y=50,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="1234",text="MENU",font="Verdana",font_size=30,font_color=(0,255,0))
        # self.boton2 = Button(master=self,x=200,y=50,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="8",text="MENU 2",font="Verdana",font_size=30,font_color=(0,255,0))
        self.lista_widget = [self.start_btn,self.option_btn]
        
    def click_select_lvl(self, parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
    def click_options(self, parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
    def click_start(self,parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)


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
        self.collition = Collition(self.ground_enemy_list,self.player_1,self.att_enemy_list,self.fruits_list)
        #PLATAFORMAS

        self.platform_list = self.config.get_platforms()
        self.enemy_bullet = EnemyFire(bullet_speed=3,firing_cooldown=50,frame_rate_ms=60,b_scale=0.3)


    # def config(self):
    #     self.config = LvlConfig(1)
    #     return self.config

    def update(self,keys):
        
        self.delta_ms = self.clock.tick(FPS)

        
        for frutita in self.fruits_list:
            frutita.update(self.delta_ms)

        for enemy_element in self.ground_enemy_list:
            enemy_element.update(self.delta_ms,self.platform_list)

            
        for att_enemy_element in self.att_enemy_list:
            att_enemy_element.update(self.delta_ms,self.platform_list)
        
        self.collition.player_collide_enemy()
        self.collition.enemy_collide_player(self.delta_ms)
        self.collition.att_enemy_sees_player()
        self.collition.player_pick_up_fruit()

        self.enemy_bullet.update(self.delta_ms)             

        self.player_1.events(self.delta_ms,keys)
        self.player_1.update(self.delta_ms,self.platform_list)

        
        if(self.player_1.get_player_score() >= 2000):
        # player_1.winning_state()
            for ground_enemy in self.ground_enemy_list:
                ground_enemy.winning_status()
            for att_enemy in self.att_enemy_list:
                att_enemy.winning_status() 
        if(self.player_1.get_player_lives() == 0):          
            if self.player_1.player_is_dead():
                self.set_active("form_death")
                self.re_init()
        self.screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())

    def draw(self):
        
        for plataforma in self.platform_list:
            plataforma.draw(self.screen)

        for frutita in self.fruits_list:
            frutita.draw(self.screen)

        for enemy_element in self.ground_enemy_list:
            enemy_element.draw(self.screen)

        for att_enemy_element in self.att_enemy_list:
            att_enemy_element.draw(self.screen)

        self.enemy_bullet.draw(self.screen)
        self.player_1.draw(self.screen)

        if(self.player_1.get_player_score() >= 2000):
            self.set_active("form_win")
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
        self.collition = Collition(self.ground_enemy_list,self.player_1,self.att_enemy_list,self.fruits_list)
        #PLATAFORMAS

        self.platform_list = self.config.get_platforms()
        self.enemy_bullet = EnemyFire(bullet_speed=3,firing_cooldown=50,frame_rate_ms=60,b_scale=0.3)



class FormOptions(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)

    #self.main_menu_ttl = 

        self.music_on_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-200,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
        self.music_off_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-100,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-300,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
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

        self.music_on_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-100,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
        self.music_off_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-200,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-300,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)

        self.resume_btn = Button(x=ANCHO_VENTANA/1.2-15,y=ALTO_VENTANA//2,text='Volver al juego',screen=master_surface,on_click=self.click_resume,on_click_param="form_start_lvl",font_size=40)
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
        
        self.music_on_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-100,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
        self.music_off_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-200,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-300,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
        self.perdiste_txt = Texts(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2+50,text='Perdiste',screen=master_surface,font_size=40)
        self.retry_btn = Button(x=ANCHO_VENTANA/1.2-15,y=ALTO_VENTANA//2+100,text='Reintentar',screen=master_surface,on_click=self.click_retry,on_click_param="menu_form",font_size=25)
                                                                                                                                                            #form_start_lvl
        self.lista_widget = [self.music_off_btn,self.music_on_btn,self.back_btn,self.retry_btn]

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
    

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
    

class FormWin(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)

        self.music_on_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
        self.music_off_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-100,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-200,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
        self.ganaste_txt = Texts(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2-300,text='Ganaste',screen=master_surface,font_size=70)
        
                                                                                                                                                     
        self.lista_widget = [self.music_off_btn,self.music_on_btn,self.back_btn,self.ganaste_txt]


    def click_music_on(self, parametro):
        pygame.mixer.music.unpause()

    def click_music_off(self, parametro):
        pygame.mixer.music.pause()

    def click_back(self,parametro):
        self.set_active(parametro)
    

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class LvlSelect(Form):
    def __init__(self,name,master_surface,x,y,active,lvl):
        super().__init__(name,master_surface,x,y,active,lvl)

        self.lvl1_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2,text='Nivel 1',screen=master_surface,on_click=self.click_lvl1,on_click_param="menu_form",font_size=40)
        self.lvl2_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2,text='Nivel 2',screen=master_surface,on_click=self.click_lvl2,on_click_param="menu_form",font_size=40)
        self.lvl3_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2,text='Nivel 3',screen=master_surface,on_click=self.click_lvl3,on_click_param="menu_form",font_size=40)
        self.back_btn = Button(x=ANCHO_VENTANA/1.2-10,y=ALTO_VENTANA//2+100,text='Volver',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
       
        
                                                                                                                                                     
        self.lista_widget = [self.lvl1_btn,self.lvl2_btn,self.back_btn,self.lvl3_btn]
    
    
    def click_lvl1(self,parametro):
        self.set_active(parametro)
        click_sound.play(0,450,0)
    def click_lvl2(self, parametro):
        pygame.mixer.music.unpause()
        click_sound.play(0,450,0)
    def click_lvl3(self, parametro):
        pygame.mixer.music.pause()
        click_sound.play(0,450,0)
    def click_back(self,parametro):
        self.set_active(parametro)
    

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()