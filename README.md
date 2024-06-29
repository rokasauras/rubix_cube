<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Rubik's Cube Solver</h1>
    <p>This repository contains a Rubik's Cube solver that uses algorithms to find the fastest possible way of solving a Rubik's Cube. Currently, the cube's state must be manually entered, but future enhancements may include using a camera to detect the unsolved cube and generating written instructions with arrows to illustrate the solution steps.</p>
    
  <h2>Features</h2>
    <ul>
        <li>Initializes a Rubik's Cube in its solved state.</li>
        <li>Supports clockwise and counterclockwise rotations for each face.</li>
        <li>Updates adjacent faces correctly after each rotation.</li>
        <li>Prints the current state of the cube for visualisation.</li>
    </ul>
    
  <h2>Future Enhancements</h2>
    <ul>
        <li>Implementing a camera-based detection system to automatically input the unsolved cube's state.</li>
        <li>Creating detailed solution instructions with arrows.</li>
        <li>Compact the code, so it generates matrices, instead of changing premade ones. Easier to visualise.</li>
    </ul>

   <h2>Installation</h2>
        <p>To use this project, ensure you have Python installed along with the NumPy library. You can install NumPy using pip:</p>
        <pre><code>pip install numpy</code></pre>
</body>
</html>
