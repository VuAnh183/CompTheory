class TuringMachine:
    def __init__(self, transitions, initial_state, accept_states):
        self.transitions = transitions
        self.current_state = initial_state
        self.accept_states = accept_states
        self.tape = ['_']  # Initialize the tape with a blank symbol
        self.head_position = 0  # Initialize the tape head position

    def step(self):
        current_symbol = self.tape[self.head_position]
        if (self.current_state, current_symbol) in self.transitions:
            new_state, new_symbol, move_direction = self.transitions[(self.current_state, current_symbol)]
            self.current_state = new_state
            self.tape[self.head_position] = new_symbol
            if move_direction == 'R':
                self.head_position += 1  # Move right
                if self.head_position == len(self.tape):
                    self.tape.append('_')  # Extend the tape if needed
            elif move_direction == 'L':
                self.head_position -= 1  # Move left
                if self.head_position < 0:
                    self.tape.insert(0, '_')  # Extend the tape to the left if needed
        else:
            raise RuntimeError("No transition defined for current state and symbol.")

    def run(self, max_steps=100):
        for _ in range(max_steps):
            if self.current_state in self.accept_states:
                return True
            self.step()
        return False

# Example usage:
transitions = {
    ('q0', '0'): ('q1', '1', 'R'),
    ('q1', '1'): ('q0', '0', 'R'),
}
initial_state = 'q0'
accept_states = {'q1'}

tm = TuringMachine(transitions, initial_state, accept_states)
input_tape = ['0', '1', '1', '0']  # Example input
tm.tape.extend(input_tape)

if tm.run():
    print("Accepted!")
else:
    print("Not accepted.")
