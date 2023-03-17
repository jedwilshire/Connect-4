import pygame
pygame.font.init()
class Writer:
    def __init__(self, screen, font = 'Arial', size = 12, color = (0, 0, 0)):
        self.screen = screen
        self.font = font
        self.size = size
        self.color = color
        self.writer = pygame.font.SysFont(self.font, self.size)
        
    def write(self, text, x, y):
        img = self.writer.render(text, True, self.color)
        self.screen.blit(img, (x, y))
        
