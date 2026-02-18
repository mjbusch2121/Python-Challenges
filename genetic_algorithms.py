import random
# constants
TARGET_PHRASE = "I love Bluegrass!" # the target phrase to be matched
POPULATION_SIZE = 250 # number of individuals in the population
MUTATION_RATE = 0.02 # probability of mutation

# generate initial population
def generate_population():
    population = []
    for _ in range(POPULATION_SIZE):
        individual = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ , .!') for _ in range(len(TARGET_PHRASE)))
        population.append(individual)
    return population

# calculate fitness score
def calculate_fitness(individual):
    score = 0
    for i in range(len(TARGET_PHRASE)):
        if individual[i] == TARGET_PHRASE[i]:
            score += 1
    return score

# select parents based on fitness
def select_parents(population):
    parents = []
    for _ in range(2):
        parents.append(max(population, key=calculate_fitness))
    return parents

# create offspring through crossover
def crossover(parents):
    offspring = ""
    crossover_point = random.randint(0, len(TARGET_PHRASE) - 1)
    for i in range(len(TARGET_PHRASE)):
        if i <= crossover_point:
            offspring += parents[0][i]
        else:
            offspring += parents[1][i]
    return offspring

# mutate offspring
def mutate(offspring):
    mutated_offspring = ""
    for i in range(len(offspring)):
        if random.random() < MUTATION_RATE:
            mutated_offspring += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ , .!')
        else:
            mutated_offspring += offspring[i]
    return mutated_offspring

# create main genetic algorithm
def genetic_algorithm():
    population = generate_population()
    generation = 1

    while True:
        print(f"Generation {generation} -Best Fit: {max(population, key=calculate_fitness)}")

        if TARGET_PHRASE in population:
            break

        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parents = select_parents(population)
            offspring = crossover(parents)
            mutated_offspring = mutate(offspring)
            new_population.extend([offspring, mutated_offspring])

        population = new_population
        generation += 1
# run the genetic algorithm
genetic_algorithm()


#This code initializes a population of random strings, evaluates their fitness scores, selects the fittest individuals as parents, performs crossover and mutation to generate new offspring, and iterates through generations until the target phrase is found or a satisfactory solution is achieved. The progress is printed after each generation to track the best fitness score.