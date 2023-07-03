import random

class Gene:
    def __init__(self, value):
        self.value = value

    def mutate(self):
        self.value = 1 - self.value

class Chromosome:
    def __init__(self):
        self.genes = [Gene(random.randint(0, 1)) for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def is_all_ones(self):
        for chromosome in self.chromosomes:
            for gene in chromosome.genes:
                if gene.value == 0:
                    return False
        return True

class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def reproduce(self):
        child_dna = DNA()
        child_dna.chromosomes = [Chromosome() for _ in range(10)]
        return Organism(child_dna, self.environment)

# Experiment
def run_experiment():
    generation = 0
    organism = Organism(DNA(), 0.1)

    while not organism.dna.is_all_ones():
        organism.mutate()
        organism = organism.reproduce()
        generation += 1

    return generation

# Run the experiment and print the results
generations = run_experiment()
print("Number of generations:", generations)
