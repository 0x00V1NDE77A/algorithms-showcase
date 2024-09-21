# utils.py

import random

# Global Variables
NUM_BARS = 50
BAR_WIDTH = 20
SPEED = 0.1
WIDTH, HEIGHT = 1000, 700

# Color schemes
COLOR_SCHEMES = [
    ((0, 0, 255), (0, 255, 0)),  # Blue-Green
    ((128, 0, 128), (255, 20, 147)),  # Purple-Pink
    ((255, 0, 0), (255, 165, 0)),  # Red-Orange
    ((255, 255, 0), (0, 0, 255))  # Yellow-Blue
]

def generate_random_array(num_bars):
    return [random.randint(10, 100) for _ in range(num_bars)]
