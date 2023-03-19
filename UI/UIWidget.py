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
        """_summary_

        Args:
            position (Tuple[int, int]): _description_
            enabled (bool, optional): _description_. Defaults to True.
        """        
        self.position = position
        self.enabled = enabled
        self.is_hovered = False

    def update(self) -> None:
        pass
