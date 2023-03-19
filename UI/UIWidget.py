from typing import Tuple

class UIWidget:
    """
    Base class for all UI Widgets
    Each UI Widget will have:
    - a position
    - enabled
    - is_hovered
    """

    def __init__(self, position: Tuple[int, int], enabled: bool = True) -> None:
        self.position = position
        self.enabled = enabled
        self.is_hovered = False

    def update(self) -> None:
        pass
