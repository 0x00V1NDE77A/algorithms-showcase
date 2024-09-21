# main.py

import pygame
from button import Button
from slider import Slider
from algorithms import bubble_sort, selection_sort, insertion_sort
from draw import draw_bars
from utils import generate_random_array, WIDTH, HEIGHT, NUM_BARS, BAR_WIDTH, COLOR_SCHEMES, SPEED

# Initialize Pygame
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Sort Menu Function
def sort_menu():
    font = pygame.font.SysFont("comicsans", 40)
    WIN.fill((255, 255, 255))  # White background

    text1 = font.render("1. Bubble Sort", True, (0, 0, 0))  # Black text
    text2 = font.render("2. Selection Sort", True, (0, 0, 0))
    text3 = font.render("3. Insertion Sort", True, (0, 0, 0))

    WIN.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 4))
    WIN.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 4 + 60))
    WIN.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT // 4 + 120))

    pygame.display.update()

    sorting_algo = None
    while sorting_algo is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sorting_algo = "bubble"
                elif event.key == pygame.K_2:
                    sorting_algo = "selection"
                elif event.key == pygame.K_3:
                    sorting_algo = "insertion"

    return sorting_algo

# Main Function
def main():
    global SPEED
    run = True
    sorting = False
    selected_algo = None

    # Generate initial array
    array = generate_random_array(NUM_BARS)
    current_color_scheme = 0

    # Buttons
    increase_speed_button = Button(WIDTH - 200, 500, 150, 50, "Speed Up", (255, 165, 0), (173, 216, 230), lambda: increase_speed())
    decrease_speed_button = Button(WIDTH - 200, 430, 150, 50, "Slow Down", (255, 165, 0), (173, 216, 230), lambda: decrease_speed())
    reset_button = Button(WIDTH - 200, 360, 150, 50, "Reset Array", (255, 165, 0), (173, 216, 230), lambda: reset_array(array))
    color_button = Button(WIDTH - 200, 290, 150, 50, "Change Colors", (255, 165, 0), (173, 216, 230), lambda: change_color_scheme())

    while run:
        if not sorting:
            selected_algo = sort_menu()
            sorting = True
            arr_copy = array[:]  # Copy array

            # Sort based on selected algorithm
            if selected_algo == "bubble":
                bubble_sort(arr_copy, SPEED, lambda arr, **kwargs: draw_bars(arr, WIN, BAR_WIDTH, HEIGHT, COLOR_SCHEMES[current_color_scheme], **kwargs))
            elif selected_algo == "selection":
                selection_sort(arr_copy, SPEED, lambda arr, **kwargs: draw_bars(arr, WIN, BAR_WIDTH, HEIGHT, COLOR_SCHEMES[current_color_scheme], **kwargs))
            elif selected_algo == "insertion":
                insertion_sort(arr_copy, SPEED, lambda arr, **kwargs: draw_bars(arr, WIN, BAR_WIDTH, HEIGHT, COLOR_SCHEMES[current_color_scheme], **kwargs))

        # Draw buttons
        increase_speed_button.draw(WIN)
        decrease_speed_button.draw(WIN)
        reset_button.draw(WIN)
        color_button.draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
