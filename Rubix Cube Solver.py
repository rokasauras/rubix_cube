'''
This will be a rubix cube solver, that will use algorithms to find the fastest possible way,
of solving a rubix cube. I will have to manually enter the data but in future I could use a camera,
and detect the unsolved cube. To show the solution I may create written instructions with arrows,
based on the solutions.
'''

import numpy as np

class rubix_cube(): #initilises a class for the solved state of the rubix cube
    def __init__(self):
        self.state = self.create_solved_state() 

    def create_solved_state(self): 
        solved_state = np.empty((6, 3, 3), dtype=str) #creates an empty array 
        colours = ['R', 'G', 'B', 'Y', 'W', 'O'] #colours of each cube face
        for i, colour in enumerate(colours): #loop that fills in each face with a colour
            solved_state[i] = np.full((3,3), colour)
        return solved_state #returns the solved faces of the rubix cube
    
    def rotate_face_clockwise(self, face):
        self.state[face] = np.rot90(self.state[face], -1) #specifies which face to rotate in the 3D array by 90 degrees
        self.rotate_adjacent_faces(face, clockwise=True)

    def rotate_face_anticlockwise(self, face):
        self.state[face] = np.rot90(self.state[face], 1)
        self.rotate_adjacent_faces(face, clockwise=False)

    def rotate_adjacent_faces(self, face, clockwise=True):
        if face == 0: # If rotating front face
            if clockwise:
                temp = self.state[1][2, :].copy() #accesses the second face, third row, of the rubix cube
                self.state[1][2, :] = self.state[5][2, :]
                self.state[5][2, :] = self.state[3][0, ::-1]
                self.state[3][0, :] = self.state[4][2, ::-1]
                self.state[4][2, :] = temp
            
            else:
                temp = self.state[1][2,:].copy()
                self.state[1][2, :] = self.state[4][2, :] #moving around the adjusted face rows
                self.state[4][2, :] = self.state[3][0, ::-1]
                self.state[3][0, :] = self.state[5][2, ::-1] #it's reversing the order of elements in the third row of the sixth face to ensure correct relative position
                self.state[5][2, :] = temp

    def print_state(self):
        for i, face in enumerate(self.state):
            print(f"Face {i}:")
            print(face)
    
cube = rubix_cube()
print("Initial State:")
cube.print_state() #should print out all faces

cube.rotate_face_clockwise(0)

print("\nState after Movements:")
cube.print_state() #prints final state after movements










    





