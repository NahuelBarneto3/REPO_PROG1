import pygame
from pygame.locals import *
from gui_widget import Widget

 
class Button(Widget):
    def __init__(self,x,y,text,screen,on_click=None,on_click_param=None,font_size=20):
        super().__init__(x,y,text,screen,font_size)
        pygame.font.init()
        self.font = pygame.font.Font(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\Fonts\Qtback.otf",self.font_size)
        self.text_image = self.font.render(self.text,True,(255,255,0))
        self.rect = self.text_image.get_rect()
        self.rect.center = (x,y)
        #self.on_click_sound = pygame.mixer.Sound()
        self.on_click = on_click
        self.on_click_param = on_click_param
        self._text = text
                
    # def render(self):
    #     image_text = self.font_sys.render(self._text,True,self.font_color,self.color_background)
    #     self.slave_surface = pygame.surface.Surface((self.w,self.h))
    #     self.slave_rect = self.slave_surface.get_rect()
    #     self.slave_rect.x = self.x
    #     self.slave_rect.y = self.y
    #     self.slave_rect_collide = pygame.Rect(self.slave_rect)
    #     self.slave_rect_collide.x += self.master_form.x
    #     self.slave_rect_collide.y += self.master_form.y
    #     self.slave_surface.fill(self.color_background)
    #     self.slave_surface.blit(image_text,(5,5))
    
    
    def button_pressed(self):
        mouse_pos = pygame.mouse.get_pos()

        #coll
        if(self.rect.collidepoint(mouse_pos)):
            if(pygame.mouse.get_pressed()[0] == 1):
                self.on_click(self.on_click_param)
                #poner el play del sonido en el momento que clickea
    '''
    for evento in lista_eventos:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if(self.slave_rect_collide.collidepoint(evento.pos)):
                        self.on_click(self.on_click_param)

            self.render()
    '''
    
    def draw(self):
        super().draw()
        
    def update(self,lista_eventos):
        self.draw()
        self.button_pressed()

class Texts(Widget):
    def __init__(self,x,y,text,screen,on_click=None,on_click_param=None,font_size=20):
        super().__init__(x,y,text,screen,font_size)
        pygame.font.init()
        self.font = pygame.font.Font(r"D:\UTN\Utn Ingreso\Prog\python_prog_I\assets\Fonts\retry.ttf",self.font_size)
        self.text_image = self.font.render(self.text,True,(255,0,255))
        self.rect = self.text_image.get_rect()
        self.rect.center = (x,y)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self._text = text

    
    
    def button_pressed(self):
        if(self.on_click_param == None):
            pass
            #poner el play del sonido en el momento que clickea

    
    def draw(self):
        super().draw()
        
    def update(self,lista_eventos):
        self.draw()
        self.button_pressed()

    

