# Particle Filter Robot Localization

## Project Overview

This project demonstrates a practical application of particle filters for robot localization using a live, interactive simulation built with Pygame. Users can observe how a particle filter estimates a robot's position as it moves through a 2D environment with obstacles and landmarks.

## Objectives

- Implement a particle filter algorithm for robot localization
- Create an interactive 2D simulation environment using Pygame
- Visualize the particle filter's estimation process in real-time
- Allow user interaction to control the robot and simulation parameters

## Requirements

- Python 3.7+
- Pygame 2.0+
- NumPy
- Pandas

## Project Structure

1. Environment Setup
2. Particle Filter Implementation
3. Robot Simulation
4. Pygame Visualization
5. User Interaction
6. Testing and Evaluation

## Detailed Instructions

### 1. Environment Setup

- Create a Pygame window (e.g., 800x600 pixels)
- Design a 2D grid-based map (e.g., 80x60 cells, where each cell is 10x10 pixels)
- Define obstacles as rectangles or polygons
- Place landmarks at specific coordinates
- Implement functions to:
  - Check if a position is valid (not in an obstacle)
  - Calculate distance between two points

### 2. Particle Filter Implementation

- Create a Particle class with properties:
  - Position (x, y)
  - Orientation (theta)
  - Weight
- Implement the following functions:
  - Initialize particles: Randomly distribute particles across valid areas
  - Update particles based on motion: Apply motion model with added noise
  - Calculate particle weights: Compare particle measurements to actual measurements
  - Resample particles: Implement a resampling algorithm
  - Estimate robot position: Calculate weighted average of particle positions

### 3. Robot Simulation

- Create a Robot class with properties:
  - True position and orientation
  - Sensor noise parameters
  - Motion noise parameters
- Implement functions for:
  - Moving the robot: Apply motion commands with added noise
  - Sensing landmarks: Calculate distances to landmarks with added noise

### 4. Pygame Visualization

- Create functions to draw:
  - The 2D map with obstacles and landmarks
  - The true robot position (as a triangle or circle)
  - Estimated robot position
  - Particles (as small dots with varying opacity based on weight)
- Implement a function to update the visualization each frame

### 5. User Interaction

- Handle keyboard inputs for:
  - Robot movement (arrow keys for forward, backward, rotate)
  - Reset simulation (R key)
  - Adjust number of particles (+ and - keys)
  - Toggle visualization options (e.g., show/hide particles, true position)
- Display current simulation parameters and stats on screen

### 6. Testing and Evaluation

- Implement functions to measure:
  - Estimation error (distance between true and estimated position)
  - Particle diversity
  - Computation time per iteration
- Display or log these metrics during the simulation

## Implementation Steps

1. Set up the Pygame project structure
2. Implement the 2D environment and drawing functions
3. Create the Robot class and basic movement functions
4. Implement the Particle class and particle filter algorithm
5. Integrate the particle filter with the robot simulation
6. Add user interaction and keyboard controls
7. Implement performance metrics and display
8. Test and refine the simulation

## Bonus Challenges

1. Add different types of sensors (e.g., lidar simulation)
2. Implement dynamic obstacles that move during the simulation
3. Create multiple robot scenarios
4. Add a path planning algorithm for autonomous navigation

## Deliverables

1. Python script(s) implementing the particle filter demo
2. README file with instructions to run the demo
3. Short report or video explaining the particle filter algorithm and demo features

## Resources

- Pygame documentation: https://www.pygame.org/docs/
- Particle filter tutorial: https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/12-Particle-Filters.ipynb
- "Probabilistic Robotics" by Thrun, Burgard, and Fox
- NumPy documentation: https://numpy.org/doc/

## Running the Demo

1. Install the required libraries: `pip install pygame numpy`
2. Run the main script: `python particle_filter_demo.py`
3. Use arrow keys to move the robot
4. Press 'R' to reset the simulation
5. Use '+' and '-' to adjust the number of particles

## Troubleshooting

- If you encounter display issues, try updating your graphics drivers
- For performance problems, reduce the number of particles or simplify the environment
