import pygame
from .Button import Button
from .TextLabel import TextLabel
from typing import Tuple

class TextButton(Button, TextLabel):
    def __init__(
        self,
        position: Tuple[int, int],
        size: Tuple[int, int],
        color: Tuple[int, int, int],
        font: pygame.font.Font,
        text: str,
        text_color: Tuple[int, int, int],
        enabled: bool = True,
    ) -> None:
        Button.__init__(self, position, size, color, enabled)
        TextLabel.__init__(self, position, font, text, text_color, enabled)

    def draw(self, screen: pygame.Surface) -> None:
        Button.draw(self, screen)
        TextLabel.draw(self, screen)
