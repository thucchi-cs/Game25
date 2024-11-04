import pygame

class Text:
    def __init__(self, font_type, font_size, text, text_color, text_box_x, text_box_y):
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(font_type, font_size)
        self.text_var = self.font.render(self.text, True, self.text_color)  
        self.textRect = self.text_var.get_rect()
        self.textRect.center = (text_box_x,text_box_y)

    
    def blit_text(self, screen):
        self.text_var = self.font.render(self.text, True, self.text_color)  
        screen.blit(self.text_var, self.textRect)
    
    