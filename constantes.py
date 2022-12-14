from pygame import mixer
import pygame

pygame.mixer.pre_init()
mixer.init()

path_lvl_1 = "./Lvls/Lvl1.json"
path_lvl_2 = "./Lvls/Lvl2.json"

ONE_SEC = 1000
ONE_MIN = 60000
#agregar en el json hasta despues del asset y lo anterior tenerlo como constante 
ANCHO_VENTANA = 1500
ALTO_VENTANA = 800
GROUND_LEVEL = 705
FPS = 60
#NOMBRES DE ASSETS PARA LOS TILES LVL2
ACID_TOP = 16
ACID_BOTTOM = 17
MOVING_Y_PLATFORM = 14
SPYKE = 15
MOVING_X_PLATFORM = 19
WALL_FACING_R = 20
WALL_FACING_L = 21

PATH_IMAGE = "./assets/images"
DIRECTION_L = 0
DIRECTION_R = 1
GROUND_COLLIDE_H = 10 # Aprox Gravedad/2 + 1

DEBUG = False

BULL_SPAWN_Y = GROUND_LEVEL-200
OUT_SCREEN_R = 1600
OUT_SCREEN_L = -100

# menu_music =pygame.mixer.music.load("./assets/WAV/Persona5OST.wav")
# menu_music =pygame.mixer.music.play(0,0,4000)
# menu_music =pygame.mixer.music.set_volume(0.2)
death_sound = pygame.mixer.Sound("./assets/WAV/enemydie.wav") 
death_sound.set_volume(0.2)
fruit_pick_up_sound = pygame.mixer.Sound("./assets/WAV/comida.wav")
fruit_pick_up_sound.set_volume(0.2)
click_sound = pygame.mixer.Sound("./assets/WAV/click.wav")
click_sound.set_volume(0.2)
win_fanfare_sound = pygame.mixer.Sound("./assets/WAV/ff7_fanfare.wav")
win_fanfare_sound.set_volume(0.1)
death_sound = pygame.mixer.Sound("./assets/WAV/a-comerlaa.wav")
death_sound.set_volume(0.1)
door_sound = pygame.mixer.Sound("./assets/WAV/door.wav")
door_sound.set_volume(0.3)