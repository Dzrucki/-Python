import pygame
import random

class Food:
    def __init__(self, screen_width, screen_height, block_size):
        self.block_size = block_size
        self.x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
        self.y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    def draw(self, display):
        pygame.draw.rect(display, (0, 255, 0), [self.x, self.y, self.block_size, self.block_size])
