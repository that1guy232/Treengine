from Trengine.ECS.System import System

from Trengine.ECS.common.components.SpriteComponent import SpriteComponent
from Trengine.ECS.common.components.PositionComponent import PositionComponent

from Trengine.ECS.Entity import Entity

from Trengine.Game.GameScene import GameScene


class SpriteRenderSystem(System):
    def __init__(self, game_scene : GameScene) -> None:
        super().__init__()

        self.game_scene = game_scene

        self.required_components = [
            "SpriteComponent",
            "PositionComponent"
        ]
        
        self.renderable_entities = []

        # get the renderable entities
        entity : Entity
        for entity in self.game_scene.ECSWorld.entities:
            if entity.has_components(self.required_components):
                self.renderable_entities.append(entity)
                pass
            pass

        pass

    def update(self, dt):
        entity : Entity
        for entity in self.renderable_entities:
            print(entity.components)
            sprite_component = entity.get_component(SpriteComponent)
            print(sprite_component)
            position_component = entity.get_component(PositionComponent)
            
            self.game_scene.game.screen.blit(sprite_component.sprite, (position_component.x, position_component.y))

        pass
    pass