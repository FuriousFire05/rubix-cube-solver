# visualizer/buttons.py

import pygame


class Button:
    def __init__(self, x, y, width, height, color, text, font_size=22):
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = color
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(None, font_size)

    def draw(self, screen):
        # Hover effect
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            # brighten slightly
            self.color = tuple(min(c + 30, 255) for c in self.base_color)
        else:
            self.color = self.base_color

        # Draw button
        pygame.draw.rect(screen, self.color, self.rect, border_radius=6)

        # Border
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=6)

        # Render text
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
        current_time = pygame.time.get_ticks()

        if current_time - self.last_switch_time > self.rotation_speed:
            self.current_color_index = (self.current_color_index + 1) % len(self.colors)
            self.last_switch_time = current_time

        color = self.colors[self.current_color_index]

        # Hover effect
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            color = tuple(min(c + 30, 255) for c in color)

        pygame.draw.rect(screen, color, self.rect, border_radius=6)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=6)

        # Auto-scale font to fit button width
        font_size = 22
        font = pygame.font.SysFont(None, font_size)

        text_surface = font.render(self.text, True, (0, 0, 0))

        # Shrink font until it fits
        while text_surface.get_width() > self.rect.width - 10 and font_size > 12:
            font_size -= 1
            font = pygame.font.SysFont(None, font_size)
            text_surface = font.render(self.text, True, (0, 0, 0))

        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
