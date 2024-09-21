# button.py

import pygame

BLACK = (0, 0, 0)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.font = pygame.font.SysFont("comicsans", 25)

    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(window, self.hover_color, self.rect)
            if clicked[0] == 1 and self.action:
                self.action()
        else:
            pygame.draw.rect(window, self.color, self.rect)

        text_surf = self.font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        window.blit(text_surf, text_rect)
