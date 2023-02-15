from ECS.Component import Component
from ECS.System import System
from ECS.Entity import Entity

# define the world
class World:
    def __init__(self):
        self.entities = []
        self.systems = []

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def add_system(self, system: System):
        self.systems.append(system)

    def update(self):
        for system in self.systems:
            system.update()