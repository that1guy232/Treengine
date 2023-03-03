import pygame

from Treengine.SM.StateMachine import StateMachine


class GameScene:
    def __init__(self, game, name) -> None:
        self.game = game
        self.name = name
        self.clear_color = (0, 0, 0)

        self.UIWidgets = []
        self.renderables = []

        self.available_states = []

        self.state_machine = StateMachine()

        pass

    def on_enter(self):
        # reset the camera
        self.game.camera.posistion = pygame.Vector2(0, 0)
        self.game.camera.zoom = 1
        pass

    def on_exit(self):
        pass

    def update(self, dt):
        # update the state machine
        self.state_machine.update(dt)
        pass

    def draw(self):
        # clear the screen
        self.game.screen.fill(self.clear_color)

        # draw all the renderables
        for renderable in self.renderables:
            renderable.draw(
                self.game.screen, self.game.camera.posistion, self.game.camera.zoom
            )
            pass

        # draw all the UI widgets
        for widget in self.UIWidgets:
            widget.draw(self.game.screen)
        pass

    def handle_event(self, event):
        for widget in self.UIWidgets:
            widget.handle_event(event)
            pass

        pass

    def add_renderable(self, renderable):
        self.renderables.append(renderable)
        pass

    def add_UIWidget(self, widget):
        self.UIWidgets.append(widget)
        pass

    pass
