import pygame

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.block_size = 10
        self.length = 1
        self.body = [[x, y]]

    def change_direction(self, direction):
        if direction == 'LEFT' and self.x_change == 0:
            self.x_change = -self.block_size
            self.y_change = 0
        elif direction == 'RIGHT' and self.x_change == 0:
            self.x_change = self.block_size
            self.y_change = 0
        elif direction == 'UP' and self.y_change == 0:
            self.y_change = -self.block_size
            self.x_change = 0
        elif direction == 'DOWN' and self.y_change == 0:
            self.y_change = self.block_size
            self.x_change = 0

    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        self.body.append([self.x, self.y])
        if len(self.body) > self.length:
            del self.body[0]

    def has_collided(self, width, height):
        if self.x >= width or self.x < 0 or self.y >= height or self.y < 0:
            return True
        for segment in self.body[:-1]:
            if segment == [self.x, self.y]:
                return True
        return False

    def eat(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            return True
        return False

    def grow(self):
        self.length += 1

    def draw(self, display):
        for segment in self.body:
            pygame.draw.rect(display, (0, 0, 0), [segment[0], segment[1], self.block_size, self.block_size])
