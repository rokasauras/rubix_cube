'''
This will be a rubix cube solver, that will use algorithms to find the fastest possible way,
of solving a rubix cube. I will have to manually enter the data but in future I could use a camera,
and detect the unsolved cube. To show the solution I may create written instructions with arrows,
based on the solutions.
'''

import numpy as np

class rubix_cube():
    def __init__(self):
        self.state = self.create_solved_state()

    def create_solved_state(self):
        solved_state = np.empty((6, 3, 3), dtype=str)
        colours = ['R', 'G', 'B', 'Y', 'W', 'O']
        for i, colour in enumerate(colours):
            solved_state[i] = colour






    





