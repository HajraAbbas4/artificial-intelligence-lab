# ---------------- Experiment 10 ----------------
# Genetic Algorithm Operations: Selection, Crossover and Mutation

import random


def fitness(chromosome):
    return sum(chromosome)


def selection(population):
    population = sorted(population, key=fitness, reverse=True)
    return population[0], population[1]


def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def mutation(chromosome):
    index = random.randint(0, len(chromosome) - 1)
    chromosome[index] = 1 - chromosome[index]
    return chromosome


population = [
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
]

print("\nExperiment 10: Genetic Algorithm")
print("Initial Population:", population)

parent1, parent2 = selection(population)
print("Selected Parents:", parent1, parent2)

child1, child2 = crossover(parent1, parent2)
print("Children after Crossover:", child1, child2)

mutated_child = mutation(child1)
print("Child after Mutation:", mutated_child)
