from pygame import mixer
import pygame

pygame.mixer.pre_init()
mixer.init()

ANCHO_VENTANA = 1500
ALTO_VENTANA = 800
GROUND_LEVEL = 705
FPS = 60

PATH_IMAGE = r"D:\UTN\Utn Ingreso\Prog\python_prog_I\jueguito\images\\"
DIRECTION_L = 0
DIRECTION_R = 1
GROUND_COLLIDE_H = 8 # Aprox Gravedad/2 + 1
DEBUG = True

pygame.mixer.music.load(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\WAV\music.wav\\")
musica_juego = pygame.mixer.music.play(0,0,4000)
musica_juego = pygame.mixer.music.set_volume(0.3)