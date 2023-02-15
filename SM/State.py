class State:
    def __init__(self, name):
        self.name = name

    def enter(self):
        print(f"Entering state {self.name}")

    def exit(self):
        print(f"Exiting state {self.name}")