from particle import Particle
import numpy as np

class Simulation:
    def __init__(self, num_particles=10, search_space=[0,1], search_func=None, cognitive=1, social=1):
        self.current_iteration = 0
        self.search_space = search_space
        self.positions = {"swarm":[],
                          "iteration":[0]}
        self.velocities = {"iteration": [0]}
        self.particles = [Particle() for _ in range(num_particles)]
        if search_func is None:
            self.f = self.test_search_function
        else:
            self.f = search_func
        self.best_swarm_position = np.mean(search_space)
        self.cognitive_learning = cognitive
        self.social_learning = social
        self.initialize_particles()

    def initialize_particles(self):
        for i, p in enumerate(self.particles):
            self.positions[str(i)] = []
            self.velocities[str(i)] = []

            position = np.random.uniform(self.search_space[0], self.search_space[1])
            velocity = np.random.uniform(-1.0, 1.0)
            p.set_position(position)
            p.set_best_position(position)
            p.set_velocity(velocity)
            if self.f(p.best_position) < self.f(self.best_swarm_position):
                self.best_swarm_position = p.best_position
            self.positions[str(i)].append(p.position)
            self.velocities[str(i)].append(p.velocity)
        self.positions["swarm"].append(self.best_swarm_position)

    def test_search_function(self, x):
        return x**2
    
    def update(self):
        for i, p in enumerate(self.particles):
            self.update_velocity(p)
            self.update_position(p)
            self.update_best_position(p)
            if self.f(p.best_position) < self.f(self.best_swarm_position):
                self.best_swarm_position = p.best_position
            self.positions[str(i)].append(p.position)
            self.velocities[str(i)].append(p.velocity)
        self.positions["swarm"].append(self.best_swarm_position)
    
    def update_velocity(self, particle:Particle):
        R_1 = np.random.uniform()
        R_2 = np.random.uniform()
        w = 0.8
        velocity = w * particle.velocity
        velocity += self.cognitive_learning*R_1*(particle.best_position - particle.position)
        velocity += self.social_learning*R_2*(self.best_swarm_position - particle.position)
        particle.velocity = velocity

    def update_position(self, particle:Particle):
        particle.position += particle.velocity

    def update_best_position(self, particle:Particle):
        if self.f(particle.position) < self.f(particle.best_position):
            particle.best_position = particle.position

    def run(self, num_iterations):
        for i in range(num_iterations):
            self.current_iteration = i+1
            self.positions["iteration"].append(self.current_iteration)
            self.velocities["iteration"].append(self.current_iteration)
            self.update()

    def step(self):
        self.current_iteration += 1
        self.positions["iteration"].append(self.current_iteration)
        self.update()