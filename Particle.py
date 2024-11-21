'''
Class: Particle

Represents a single particle used in the particle filter.

Attributes:
    position (tuple): The particle's current position (x, y).
    orientation (float): The particle's current orientation in radians.
    weight (float): The weight of the particle based on its likelihood given the sensor measurements.
Methods:
    move(delta_distance, delta_angle): Updates the particle's position and orientation based on motion commands with added noise.
    calculate_weight(measurement, landmarks): Updates the particle's weight based on a comparison between its predicted sensor measurements and actual measurements.
'''

class Particle():
    def __init__():
        pass