# visualizer/buttons.py

import pygame


class Button:
    def __init__(self, x, y, width, height, color, text, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


class RotatingColorButton:
    def __init__(self, x, y, width, height, colors, text, rotation_speed=500):
        self.rect = pygame.Rect(x, y, width, height)
        self.colors = colors
        self.current_color_index = 0
        self.text = text
        self.font = pygame.font.SysFont(None, 24)
        self.last_switch_time = pygame.time.get_ticks()
        self.rotation_speed = rotation_speed  # in milliseconds

    def draw(self, screen):
        # Time-based color rotation
        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch_time > self.rotation_speed:
            self.current_color_index = (self.current_color_index + 1) % len(self.colors)
            self.last_switch_time = current_time

        color = self.colors[self.current_color_index]

        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
