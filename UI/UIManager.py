from UI import UIWidget


import pygame

class UIManager:
    def __init__(self) -> None:
        self.UIWidget = []

    # Add widget and enforce UIWidget type
    def add_widget(self, widget: UIWidget) -> None:
        self.UIWidgets.append(widget)

    
    def handle_event(self, event: pygame.event.Event) -> None:
        for widget in self.UIWidgets:
            widget.handle_event(event)

    def update(self) -> None:
        for widget in self.UIWidgets:
            widget.update()

    def draw(self, screen: pygame.Surface) -> None:
        for widget in self.UIWidgets:
            widget.draw(screen)