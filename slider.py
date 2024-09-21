# slider.py

import pygame
ORANGE = (255, 165, 0)

class Slider:
    def __init__(self, x, y, width, min_value, max_value):
        self.rect = pygame.Rect(x, y, width, 10)
        self.circle_x = x
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value
        self.dragging = False

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 0), self.rect)
        pygame.draw.circle(window, ORANGE, (self.circle_x, self.rect.centery), 15)
        if self.dragging:
            mouse_x = pygame.mouse.get_pos()[0]
            self.circle_x = max(self.rect.x, min(mouse_x, self.rect.x + self.rect.width))
            self.value = self.min_value + (self.circle_x - self.rect.x) / self.rect.width * (self.max_value - self.min_value)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
