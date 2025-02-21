import numpy as np

class Particle:
    def __init__(self):
        self.position = np.random.uniform()
        self.velocity = np.random.uniform(-1.0, 1.0)
        self.best_position = self.position

    def set_position(self, X):
        self.position = X

    def set_best_position(self, X):
        self.best_position = X

    def set_velocity(self, V):
        self.velocity = V

    def __str__(self):
        return f"{self.position}, {self.velocity}, {self.best_position}"