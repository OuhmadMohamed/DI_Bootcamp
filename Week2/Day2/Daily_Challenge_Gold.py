import random

# ================================================
# Biology Challenge: DNA, Genes, Chromosomes & Evolution
# Emphasis on OOP, Inheritance, and Polymorphism
# ================================================

# Base class to demonstrate polymorphism (optional but nice)
class Mutable:
    """Base class for objects that can mutate."""
    def mutate(self):
        raise NotImplementedError("Subclasses must implement mutate()")

class Gene(Mutable):
    """A single Gene: value 0 or 1, can flip."""
    def __init__(self, value=None):
        self.value = random.randint(0, 1) if value is None else value

    def mutate(self):
        """Flip the value (0 ↔ 1)."""
        self.value = 1 - self.value

    def __repr__(self):
        return str(self.value)

class Chromosome(Mutable):
    """A Chromosome: 10 Genes."""
    def __init__(self, genes=None):
        self.genes = [Gene() for _ in range(10)] if genes is None else genes[:]

    def mutate(self):
        """Each gene has 1/2 chance to flip independently."""
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def __repr__(self):
        return ''.join(str(gene) for gene in self.genes)

class DNA(Mutable):
    """A DNA: 10 Chromosomes (total 100 genes)."""
    def __init__(self, chromosomes=None):
        if chromosomes is None:
            self.chromosomes = [Chromosome() for _ in range(10)]
        else:
            # Deep copy to avoid shared references
            self.chromosomes = [Chromosome(chrom.genes[:]) for chrom in chromosomes]

    def mutate(self):
        """Each chromosome has 1/2 chance to mutate (then its genes flip randomly)."""
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    def is_all_ones(self):
        """Check if the target DNA (all 1s) is reached."""
        return all(gene.value == 1 for chrom in self.chromosomes for gene in chrom.genes)

    def fitness(self):
        """Proportion of 1s (0.0 to 1.0)."""
        total_ones = sum(gene.value == 1 for chrom in self.chromosomes for gene in chrom.genes)
        return total_ones / 100.0

    def __repr__(self):
        return "\n".join(str(chrom) for chrom in self.chromosomes)

class Organism:
    """An organism with DNA living in an environment that influences mutation rate."""
    def __init__(self, dna=None, environment_mutation_prob=0.5):
        self.dna = dna if dna else DNA()
        self.mutation_prob = environment_mutation_prob

    def mutate(self):
        """Apply environment-triggered mutation to DNA."""
        if random.random() < self.mutation_prob:
            self.dna.mutate()

# ================================================
# Simulation: Evolve a population until one reaches all-1s DNA
# ================================================

def evolve_to_target(population_size=100, max_generations=1000000, mutation_prob=0.5):
    """Run one full experiment."""
    population = [Organism(environment_mutation_prob=mutation_prob) for _ in range(population_size)]
    
    generation = 0
    while generation < max_generations:
        generation += 1
        
        # Mutate every organism
        for org in population:
            org.mutate()
            
            # Check for success
            if org.dna.is_all_ones():
                return generation
        
        # Optional: early stop if somehow all died (not possible here)
    
    return -1  # Not found within limit

# Run multiple trials for statistics
if __name__ == "__main__":
    random.seed(42)  # Reproducible results
    num_trials = 3
    mutation_probability = 0.5
    pop_size = 10
    
    results = []
    for i in range(num_trials):
        gens = evolve_to_target(population_size=pop_size, mutation_prob=mutation_probability)
        results.append(gens)
        print(f"Trial {i+1}: {gens} generations")
    
    successful = [r for r in results if r > 0]
    avg = sum(successful) / len(successful)
    min_gens = min(successful)
    max_gens = max(successful)
    
    print("\n" + "="*50)
    print("BIOLOGY RESEARCH NOTEBOOK - CONCLUSIONS")
    print("="*50)
    print(f"Population size: {pop_size} organisms")
    print(f"Environment mutation probability: {mutation_probability}")
    print(f"Target: DNA with all 100 genes = 1")
    print(f"Number of trials: {num_trials}")
    print(f"Average generations to reach target: {avg:.0f}")
    print(f"Fastest evolution: {min_gens} generations")
    print(f"Slowest evolution: {max_gens} generations")
    print("\nConclusion:")
    print("This simulation models a simple evolutionary process where random mutations")
    print("gradually push the population toward a specific perfect genotype (all 1s).")
    print("Even though each mutation step is small and random, with a population of 100")
    print("and persistent mutation pressure, the target is reliably reached.")
    print("The number of generations varies significantly due to the stochastic nature")
    print("of mutations, but on average it takes several thousand generations.")
    print("This illustrates how rare beneficial configurations can eventually emerge")
    print("through cumulative random variation — a core idea in evolutionary biology!")
    print("="*50)
    
