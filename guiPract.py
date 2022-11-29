import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import FormMenu

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA),flags,16)
pygame.init()
clock = pygame.time.Clock()


form_menu = FormMenu(master_surface=screen,x=100,y=100,w=400,h=400,background_color=(255,255,0),border_color=(255,0,255),active=True)
form_menu2 = FormMenu(master_surface=screen,x=400,y=100,w=400,h=400,background_color=(0,255,255),border_color=(255,0,255),active=True)

while True:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)


    if(form_menu.active):
        form_menu.update(lista_eventos)
        form_menu.draw()
    
    if(form_menu.active):
        form_menu.update(lista_eventos)
        form_menu.draw()
        
    pygame.display.flip()


