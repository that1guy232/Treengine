class StateMachine:
    def __init__(self) -> None:
        self.states = {}
        self.current_state = None
        pass

    def add_state(self, name, state):
        self.states[name] = state
        pass


    pass

