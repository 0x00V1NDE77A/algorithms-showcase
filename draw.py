# draw.py

import pygame

# Draw gradient for the bars
def draw_gradient_rect(window, rect, color1, color2):
    for i in range(rect.height):
        color = [
            color1[j] + (color2[j] - color1[j]) * (i / rect.height)
            for j in range(3)
        ]
        pygame.draw.line(window, color, (rect.x, rect.y + i), (rect.x + rect.width, rect.y + i))

# Draw the bars of the array
def draw_bars(arr, WIN, BAR_WIDTH, HEIGHT, colors, highlight_index=None, compare_index=None, message=""):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    WIN.fill(WHITE)

    color1, color2 = colors

    for i, value in enumerate(arr):
        x = i * BAR_WIDTH
        height = value * 5
        bar_color1 = color1
        bar_color2 = color2
        if i == highlight_index:
            bar_color1 = BLACK
            bar_color2 = (255, 0, 0)
        elif i == compare_index:
            bar_color1 = (255, 165, 0)
            bar_color2 = (255, 20, 147)

        rect = pygame.Rect(x, HEIGHT - height, BAR_WIDTH - 2, height)
        draw_gradient_rect(WIN, rect, bar_color1, bar_color2)

    font = pygame.font.SysFont("comicsans", 20)
    text = font.render(message, True, BLACK)
    WIN.blit(text, (10, 10))
    pygame.display.update()
