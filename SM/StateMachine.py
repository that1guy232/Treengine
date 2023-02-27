from .State import State as State


class StateMachine:
    def __init__(self) -> None:
        self.states = {}
        self.state_stack = []
        pass

    def push_state(self, state: State):
        self.state_stack.append(state)
        state.on_enter()
        pass

    def pop_state(self, state: State = None):
        if state == None:
            self.state_stack[-1].on_exit()
            self.state_stack.pop()

        else:
            # find the state in the stack
            for i in range(len(self.state_stack)):
                if self.state_stack[i] == state:
                    self.state_stack[i].on_exit()
                    self.state_stack.pop(i)
                    break
                pass
        pass

    # a function to determine if a state is on the stack
    def is_state_on_stack(self, state: State):
        return state in self.state_stack
        pass

    def update(self, dt=0):
        # if there is a state on the stack, update it
        if len(self.state_stack) > 0:
            # update the current state
            self.state_stack[-1].update(dt)
        pass

    pass
