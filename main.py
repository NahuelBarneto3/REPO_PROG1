import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from enemigo import Enemy
from plataforma import Plataform 
from collitions import Collition
from lvl1_platforms import import_platforms
from Lvl1_enemies import import_ground_enemies
from lvl1_Att_enemies import import_attacking_enemies
from Enemy_fire import EnemyFire
from lvl1_frutifrutonas import import_fruits
from fruits import Fruits
flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()




imagen_fondo = pygame.image.load(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\jueguito\images\locations\mountain\all.png\\").convert()

imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
#ENEMIGOS
ground_enemy_list = import_ground_enemies()
att_enemy_list = import_attacking_enemies()
#FRUTAS
fruits_list = import_fruits()
#PLAYER
player_1 = Player(x=10,y=463,speed_walk=8,speed_run=12,gravity=16,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)
collition = Collition(ground_enemy_list,player_1,att_enemy_list,fruits_list)
#PLATAFORMAS
platform_list = import_platforms()
enemy_bullet = EnemyFire(bullet_speed=3,firing_cooldown=50,frame_rate_ms=60,b_scale=0.3)




while True:     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())

    for plataforma in platform_list:
        plataforma.draw(screen)
    
    for frutita in fruits_list:
        frutita.update(delta_ms)
        frutita.draw(screen)

    for enemy_element in ground_enemy_list:
        enemy_element.update(delta_ms,platform_list)
        enemy_element.draw(screen)
        
    for att_enemy_element in att_enemy_list:
        if(not collition.att_enemy_sees_player == True):
            att_enemy_element.update(delta_ms,platform_list)
        att_enemy_element.draw(screen)
    
    collition.player_collide_enemy()
    collition.enemy_collide_player(delta_ms)
    collition.att_enemy_sees_player()
    collition.player_pick_up_fruit()
    # lives_text = player_1.draw_lives()
    # score_text =  player_1.draw_score()
    # screen.blit()
    # screen.blit(score_text,(10,10))
    
    enemy_bullet.update(delta_ms)             
    enemy_bullet.draw(screen) 
    player_1.events(delta_ms,keys)
    player_1.update(delta_ms,platform_list)
    player_1.draw(screen)
    
    if(player_1.get_player_score() >= 1500):
        player_1.draw_player_won(screen)
       # player_1.winning_state()
        for ground_enemy in ground_enemy_list:
            ground_enemy.winning_status()
        for att_enemy in att_enemy_list:
            att_enemy.winning_status() 

    #print(delta_ms)
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    #print(delta_ms)



    


  



