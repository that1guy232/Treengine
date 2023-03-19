
from .UIWidget import UIWidget

import pygame
from typing import Tuple

class Button(UIWidget):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], color: Tuple[int, int, int], enabled: bool = True) -> None:
        super().__init__(position, enabled)
        self.size = size
        self.color = color
        self.rect = pygame.Rect(position, size)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
