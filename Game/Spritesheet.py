import pygame
'''
#TODO: Should SpriteSheet have it's own TileDict?
We could have a InitTile Function that
would take a name and a x,y, flags
Than add that to a built in TileDict that could also be initialized 
with a file path or just be a empty dict
'''

class SpriteSheet:
    def __init__(self, filename, tile_size, tile_padding):
        """_summary_

        Args:
            filename (_type_): _description_
            tile_size (_type_): _description_
            tile_padding (_type_): _description_
        """
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.tile_size = tile_size
        self.tile_padding = tile_padding

    def get_tile(self, x, y):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.sheet.subsurface(
            (
                x * self.tile_size + x * self.tile_padding,
                y * self.tile_size + y * self.tile_padding,
                self.tile_size,
                self.tile_size,
            )
        )
