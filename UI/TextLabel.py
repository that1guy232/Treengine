import pygame
from .UIWidget import UIWidget
from typing import Tuple

class TextLabel(UIWidget):
    """_summary_

    Args:
        UIWidget (_type_): _description_
    """    
    def __init__(
        self,
        position: Tuple[int, int],
        font: pygame.font.Font,
        text: str,
        color: Tuple[int, int, int],
        enabled: bool = True,
    ) -> None:
        """_summary_

        Args:
            position (Tuple[int, int]): _description_
            font (pygame.font.Font): _description_
            text (str): _description_
            color (Tuple[int, int, int]): _description_
            enabled (bool, optional): _description_. Defaults to True.
        """        
        super().__init__(position, enabled)
        self.font = font
        self.text = text
        self.color = color
        self.text_surface = self.font.render(self.text, True, self.color)

    def set_text(self, text: str) -> None:
        self.text = text
        self.text_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.text_surface, self.position)
