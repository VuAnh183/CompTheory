# Turing machine 
# General idea: Input ----> Some operations ----> Output
# Basic Component:
# Head: Kinda like a pointer that moves left or right through each cells to read and write symbols
# Tape: An infinite tape that divided into discrete cells, each cells can hold a single symbol from a finite set (alphabet)
# | 1 | 0 | 0 | 1 | 1 | 0 | --> This is a tape
#    <- ô ->                --> this is a head that moves through each cells (left or right)
# State: A program that determines what the machine does (the "Some operations" part)
# State breakdown:
# Inital state: start of the machine, based on the machine state and the content of the cells that is being pointed
# State transition: perform read(mandatory) and write(optional) and move the head to another cells(also optional)
# Halt state: end of the machine, stop the machine from looping forever 
# Example:
# State machine: q0 -------> q1 <-------> q2 
# | 1 | 0 | 0 | 1 | 1 | 0 |
#   ô
# q0 to q1: read the cells, change 1 to 0 and move right
# | 0 | 0 | 0 | 1 | 1 | 0 |
#       ô
# q1 to q2: read the cells, if 1 HALT, if 0 change to 1 and move right
# | 0 | 0 | 0 | 1 | 1 | 0 |
#           ô
# q2 to q1: read the cells, change 0 to 1 and move left
# | 0 | 0 | 1 | 1 | 1 | 0 |
#       ô
# => This is just some random operations i came up with, adjust to your need when coding 

from array import *

class TuringMachine:
    def __init__(self, transitions, init_state, accept_states, input_tape):
        self.transitions = transitions
        self.current_state = init_state
        self.accept_states = accept_states
        self.input_tape = input_tape
        self.x_tape = [""] # Initialize the x tape with a blank symbol
        self.y_tape = [""] # Initialize the y tape with a blank symbol
        self.head = 0 # Initialize the tape head postion
    
    # Define what the turing machine does
    def step(self):
      current_state = self.transitions[0][0]
      input_symbol = self.transitions[0][1]
      
      match current_state:
        case "q0":
          if(input_symbol == "1" and input_symbol == "0"):
            self.tape.append(input_symbol)
            if(move_direction)
          else:
            exit()
        
        case "q1":
          if(input_symbol == "1" and input_symbol == "0"):
            self.tape.append(input_symbol)
            
            
        case "q2":
          if(input_symbol == "1" and input_symbol == "0"):
            self.tape.append(input_symbol)
          
          
        
transitions = [
  ("q0", "1", "0", "R", "q1"),
  ("q0", "0", "0", "R", "q1"),
  ("q0", "#", "0", "H", "qH"),
  ("q1", "1", "0", "R", "q1"),
  ("q1", "0", "0", "R", "q1"),
  ("q1", "#", "0", "R", "q2"),
  ("q2", "1", "0", "R", "q2"),
  ("q2", "0", "0", "R", "q2"),
  ("q2", "#", "0", "R", "q3"), 
  ("q3", "1", "0", "R", "q3"), 
  ("q3", "0", "0", "R", "q3"), 
  ("q3", "#", "0", "R", "q4"),
  ("q4", "0", "0", "0", "q5"), 
  ("q5", "0", "0", "0", "q6"), 
  ("q6", "0", "1", "R", "q6"), 
  ("q6", "0", "0", "R", "q6"),
  ("q6", "#", "#", "H", "qH")
  
]

init_state = "q0"
accept_states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"]
input_tape = ["1", "0", "1", "#", "1", "1", "1"]

tm = TuringMachine(transitions, init_state, accept_states, input_tape)
tm.step()


     
        





