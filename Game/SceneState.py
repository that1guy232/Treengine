from Treengine.SM.State import State


class SceneState(State):
    def __init__(self, name, scene) -> None:
        super().__init__(name)
        self.scene = scene

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def update(self, dt):
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        pass
