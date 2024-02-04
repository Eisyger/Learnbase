import time
import random

class Particle:
    def __init__(self, color: str, duration: int ):
        self.color = color
        self.duration = duration
        self.is_in_use = False

    def sparkle(self):
        for i in range(self.duration):
            print(f"SPARLKE in {self.color}")
            time.sleep(0.3)

class ParticlePool:
    def __init__(self, max_particles):
        self.max_particles = max_particles
        self._colors = ["blue", "red", "yellow"]
        self._pool = [Particle(self._colors[0], 0) for _ in range(max_particles)]

    def use(self):
        for part in self._pool:
            if not part.is_in_use:
                part.is_in_use = True
                return part
        raise IndexError

    def enter(self, particle):
        if particle in self._pool:
            particle.is_in_use = False


if __name__ == "__main__":
    pool = ParticlePool(2)
    part1 = pool.use()
    part2 = pool.use()
    part1.color = "red"
    part2.color = "blue"
    part1.duration = 1
    part2.duration = 2
    part1.sparkle()
    part2.sparkle()
    pool.enter(part1)
    part3 = pool.use()
    part3.color = "violett"
    part3.duration = 3
    part3.sparkle()

