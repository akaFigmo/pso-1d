from simulation import Simulation

if __name__ == "__main__":
    num_iterations = 10
    num_particles = 2

    sim = Simulation(num_particles)
    sim.run(num_iterations)