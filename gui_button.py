import pygame
from pygame.locals import *
from gui_widget import Widget

 
class Button(Widget):
    def __init__(self,x,y,text,screen,on_click=None,on_click_param=None,font_size=20):
        super().__init__(x,y,text,screen,font_size)
        pygame.font.init()
        self.font = pygame.font.Font("./assets/Fonts/Qtback.otf",self.font_size)
        self.image = self.font.render(self.text,True,(255,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        #self.on_click_sound = pygame.mixer.Sound()
        self.on_click = on_click
        self.on_click_param = on_click_param
        self._text = text
        self.last_pressed = pygame.time.get_ticks()
        self.click_cooldown = 50
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

            last_pressed_btn = pygame.time.get_ticks()
            if(last_pressed_btn - self.last_pressed >= self.click_cooldown):
                mouse_pos = pygame.mouse.get_pos()
                self.last_pressed = last_pressed_btn
                if(self.rect.collidepoint(mouse_pos)):
                    if(pygame.mouse.get_pressed()[0] == 1):
                        pygame.time.delay(200)
                        #time.sleep(0.2)
                        self.on_click(self.on_click_param)
        
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
        self.font = pygame.font.Font(r"./assets/Fonts/Qtback.otf",self.font_size)
        self.image = self.font.render(self.text,True,(255,255,255))
        self.rect = self.image.get_rect()
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

    

class TextBox(Widget):
    def __init__(self,x,y,text,screen,on_click=None,on_click_param=None,font_size=20):
        super().__init__(x,y,text,screen,font_size)
        self.font = pygame.font.Font("./assets/Fonts/Qtback.otf",font_size)
        self.image = self.font.render(text,True,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.write_on =True
        self._writing=""
        self.img_writing = self.font.render(self._writing,True,(255,255,0))
        self.rect_writing = self.img_writing.get_rect()
        self.rect_writing.center = (x,y)

    def write(self, event_list):
        for event in event_list:
                        
            if (event.type == pygame.KEYDOWN and self.write_on):
                
                if event.key == pygame.K_BACKSPACE:
                    self._writing = self._writing[:-1]
                else:
                    self._writing += event.unicode


    def draw(self):
        super().draw()
        self.image.blit(self.screen,(self.rect_writing.x,self.rect_writing.y))

    def update(self,event_list):
        self.draw()
        self.write(event_list) 