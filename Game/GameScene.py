class GameScene():
    def __init__(self, game,name) -> None:
        self.game = game
        self.name = name
        self.UIWidgets = []

        pass

    def update(self, dt):
        pass

    def draw(self):
        # clear the screen
        self.game.screen.fill((0, 0, 0))

        for widget in self.UIWidgets:
            widget.draw(self.game.screen)
        pass

    def handle_event(self, event):

        for widget in self.UIWidgets:
            widget.handle_event(event)
            pass
        
        pass

    pass