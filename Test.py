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
        self.tape = [""] # Initialize a tape with a blank symbol
        self.head = 0 # Initialize the tape head postion
    
    # Define what the turing machine does
    def step(self):
      step = 0
      x_value = 0
      n = 0
      print(self.input_tape)
      while step < len(self.transitions):
        new_state = self.transitions[step][0]
        input_symbol = self.transitions[step][1]
        output_symbol = self.transitions[step][2]
        move_direction = self.transitions[step][3]
        next_state = self.transitions[step][4]
        
        print(f"Step {step}")
        print(self.current_state, new_state, self.input_tape[self.head])
        if(self.current_state == new_state):
             
          if(self.input_tape[self.head] == input_symbol):
            # q0: is the initial state, stop if the initial symbol is #
            if(self.current_state == "q0"):
              if(self.input_tape[self.head] == "#"):
                print("End")
                break
              else:
                self.current_state = next_state
                step += 1
                continue
                  
            # q1: move to right until the symbol # is found, after that move left to get all symbols of x      
            if(self.current_state == "q1"):
              print(self.transitions[step])
              print("Reach q1! Current_state: " + self.current_state + " Head symbol: " + self.input_tape[self.head])
              if(self.input_tape[self.head] == "1" or self.input_tape[self.head] == "0"):
                print(self.input_tape[self.head])
                print(self.current_state)
                self.head += 1
              elif(self.input_tape[self.head] == "#"):
                current_state = new_state
            
          # # q2: move left to convert x to decimal      
          # if(self.current_state == "q2"):
          #   print("Reach q1: " + self.current_state)
          #   n += 1
          #   if(self.input_tape[self.head] == "1"):
          #     print("new x value:" + x_value)
          #     x_value += pow(2, n)
          #     if(move_direction == "L"):
          #       if(self.head <= 0):
          #         current_state = new_state
          #       self.head -= 1
                           
        step += 1


        
transitions = [
  ("q0", "1", "0", "H", "q1"),
  ("q0", "0", "0", "H", "q1"),
  ("q0", "#", "0", "H", "qH"),
  ("q1", "1", "0", "R", "q1"),
  ("q1", "0", "0", "R", "q1"),
  ("q1", "#", "0", "R", "q2"),
  ("q2", "1", "0", "R", "q2"),
  # ("q2", "0", "0", "R", "q2"),
  # ("q2", "#", "0", "R", "q3"), 
  # ("q3", "1", "0", "R", "q3"), 
  # ("q3", "0", "0", "R", "q3"), 
  # ("q3", "#", "0", "R", "q4"),
  # ("q4", "0", "0", "0", "q5"), 
  # ("q5", "0", "0", "0", "q6"), 
  # ("q6", "0", "1", "R", "q6"), 
  # ("q6", "0", "0", "R", "q6"),
  # ("q6", "#", "#", "H", "qH")
  
]

init_state = "q0"
accept_states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"]
input_tape = ["1", "0", "1", "#", "1", "1", "1"]

tm = TuringMachine(transitions, init_state, accept_states, input_tape)
tm.step()


     
        





