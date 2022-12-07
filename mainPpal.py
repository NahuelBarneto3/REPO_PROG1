import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from enemigo import Enemy
from plataforma import Plataform 
from collitions import Collition

from Enemy_fire import EnemyFire
from fruits import Fruits
from lvl_Config import LvlConfig
from gui_form import *
import warnings 

warnings.filterwarnings("ignore")

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()



menu_form = FormMenu(name="menu_form",master_surface=screen,x=0,y=0,active=True,lvl=1)
option_form = FormOptions(name="option_form",master_surface=screen,x=0,y=0,active=True,lvl=1)
form_start_lvl = FormLvlStart(name="form_start_lvl",master_surface=screen,x=0,y=0,active=True,lvl=2)
form_pause = FormPause(name="form_pause",master_surface=screen,x=0,y=0,active=True,lvl=1)
form_death = FormDeath(name="form_death",master_surface=screen,x=0,y=0,active=True,lvl=1)
form_win = FormWin(name="form_win",master_surface=screen,x=0,y=0,active=True,lvl=1)
form_lvl_select = FormLvlSelect(name="form_lvl_select",master_surface=screen,x=0,y=0,active=True,lvl=1)


while True:     
    
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_ESCAPE):
                #print("ESCAPE") 
                form_pause.set_active("form_pause")


    keys = pygame.key.get_pressed()

    if(menu_form.active):
        menu_form.update(lista_eventos)
        menu_form.draw()

    elif(form_start_lvl.active):
        form_start_lvl.update(keys)
        form_start_lvl.draw()
    elif(option_form.active):
        option_form.update(keys)
        option_form.draw()
    elif(form_pause.active):
        form_pause.update(keys)
        form_pause.draw()
    elif(form_death.active):
        form_death.update(lista_eventos)
        form_death.draw()
    elif(form_win.active):
        form_win.update(lista_eventos)
        form_win.draw()
    elif(form_lvl_select.active):
        form_lvl_select.update(lista_eventos)
        form_lvl_select.draw()
        if(form_lvl_select.is_selected):
            lvl = form_lvl_select.selected_lvl
            form_lvl_select.is_selected = False
            form_start_lvl = FormLvlStart(name="form_start_lvl",master_surface=screen,x=0,y=0,active=True,lvl=lvl)
        


    # screen.blit(imagen_fondo,imagen_fondo.get_rect())

    # for plataforma in platform_list:
    #     plataforma.draw(screen)
    
    # for frutita in fruits_list:
    #     frutita.update(delta_ms)
    #     frutita.draw(screen)

    # for enemy_element in ground_enemy_list:
    #     enemy_element.update(delta_ms,platform_list)
    #     enemy_element.draw(screen)
        
    # for att_enemy_element in att_enemy_list:
        
    #     att_enemy_element.update(delta_ms,platform_list)
    #     att_enemy_element.draw(screen)
    
    # collition.player_collide_enemy()
    # collition.enemy_collide_player(delta_ms)
    # collition.att_enemy_sees_player()
    # collition.player_pick_up_fruit()
    # # lives_text = player_1.draw_lives()
    # # score_text =  player_1.draw_score()
    # # screen.blit()
    # # screen.blit(score_text,(10,10))
    
    # enemy_bullet.update(delta_ms)             
    # enemy_bullet.draw(screen) 
    # player_1.events(delta_ms,keys)
    # player_1.update(delta_ms,platform_list)
    # player_1.draw(screen)
    
    # if(player_1.get_player_score() >= 2000):
    #     player_1.draw_player_won(screen)
    #    # player_1.winning_state()
    #     for ground_enemy in ground_enemy_list:
    #         ground_enemy.winning_status()
    #     for att_enemy in att_enemy_list:
    #         att_enemy.winning_status() 

    #print(delta_ms)
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    #print(delta_ms)



    


  



