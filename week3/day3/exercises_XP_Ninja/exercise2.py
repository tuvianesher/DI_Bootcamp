import random

class QuantumParticle:
    def __init__(self, x=None, p=None):
        self.position = x if x is not None else self.generate_random_position()
        self.momentum = p if p is not None else self.generate_random_momentum()
        self.spin = self.generate_random_spin()

    def position(self):
        self.disturb()
        return self.position

    def momentum(self):
        self.disturb()
        return self.momentum

    def spin(self):
        self.disturb()
        return self.spin

    def disturb(self):
        self.position = self.generate_random_position()
        self.momentum = self.generate_random_momentum()
        print('Quantum Interferences!!')

    def generate_random_position(self):
        return random.randint(1, 10000)

    def generate_random_momentum(self):
        return random.uniform(0, 1)

    def generate_random_spin(self):
        return random.choice([-0.5, 0.5])

    def entangle(self, other_particle):
        if isinstance(other_particle, QuantumParticle):
            self.spin = -self.spin
            other_particle.spin = -self.spin
            print('Particle p1 is now in quantum entanglement with Particle p2')
        else:
            print('Spooky Action at a Distance!')

    def __repr__(self):
        return f'QuantumParticle(position={self.position}, momentum={self.momentum}, spin={self.spin})'
