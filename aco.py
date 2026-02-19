import numpy as np

# define the distance matrix
distance_matrix = np.array(
    [
        [0, 7, 3, 9, 4],
        [7, 0, 5, 2, 8],
        [3, 5, 0, 6, 1],
        [9, 2, 6, 0, 7],
        [4, 8, 1, 7, 0],
    ]
)

# number of cities
num_cities = distance_matrix.shape[0]

# number of ants
num_ants = 20


def ant_colony_optimization(num_iterations):
    # initialize pheromone level matrix
    pheromone_level = np.ones((num_cities, num_cities))
    # initialize heuristic information matrix
    heuristic_info = 1 / (
        distance_matrix + np.finfo(float).eps
    )  # avoid division by zero
    # alpha and beta parameters
    alpha = 1.0  # pheromone importance
    beta = 0.5  # heuristic importance
    # initialize best path and distance
    best_distance = float("inf")
    best_path = []
    best_iteration = -1  # Initialize the best_iteration variable
    for iteration in range(num_iterations):
        # initialize ant paths and distances
        ant_paths = np.zeros((num_ants, num_cities), dtype=int)
        ant_distances = np.zeros(num_ants)
        for ant in range(num_ants):
            # choose the starting city randomly
            current_city = np.random.randint(num_cities)
            visited = [current_city]

            # construct the path
            for _ in range(num_cities - 1):
                # calculate the selection probabilities
                selection_probs = (pheromone_level[current_city] ** alpha) * (
                    heuristic_info[current_city] ** beta
                )
                selection_probs[np.array(visited)] = (
                    0  # set selection probabilities of visited cities to 0
                )
                # choose the next city based on the selection probabilities
                next_city = np.random.choice(
                    np.arange(num_cities), p=(selection_probs / np.sum(selection_probs))
                )
                # update the path and visited list
                ant_paths[ant, _ + 1] = next_city
                visited.append(next_city)
                # update the distance
                ant_distances[ant] += distance_matrix[current_city, next_city]
                # update the current city
                current_city = next_city
            # update the distance to return to next starting city
            ant_distances[ant] += distance_matrix[current_city, ant_paths[ant, 0]]
        # update the pheromone level based on the ant paths
        pheromone_level *= 0.5  # evaporation
        for ant in range(num_ants):
            for city in range(num_cities - 1):
                pheromone_level[ant_paths[ant, city], ant_paths[ant, city + 1]] += (
                    1 / ant_distances[ant]
                )
            pheromone_level[ant_paths[ant, -1], ant_paths[ant, 0]] += (
                1 / ant_distances[ant]
            )
        # update the best path and distance if a better solution is found
        min_distance_idx = np.argmin(ant_distances)
        if ant_distances[min_distance_idx] < best_distance:
            best_distance = ant_distances[min_distance_idx]
            best_path = ant_paths[min_distance_idx]
            best_iteration = iteration # update the best iteration
    return best_path, best_distance, best_iteration


# run the ant colony optimization algorithm
num_iterations = 250
best_path, best_distance, best_iteration = ant_colony_optimization(num_iterations)
# display the best path and distance
print("Here is the best path:", best_path)
print("here is the best distance:", best_distance)
print("Iteration with the best distance:", best_iteration)


# Iteration 1:
#  1. 10 ants wander randomly (no pheromone guidance yet)
#  2. Some find okay routes, some find bad routes
#  3. Evaporate all pheromones by 50%
#  4. Good routes get more pheromone reinforcement

# Iteration 2:
#  1. 10 new ants use pheromone trails to guide them
#  2. They're smarter now! They prefer proven paths
#  3. Evaporate again
#  4. Reinforce even better

# Iteration 3, 4, 5... 100:
#  - Pheromones converge on the best routes
#  - Ants mostly follow the optimal path
#  - Occasional exploration still happens (randomness)

# Final Result:
#  - The path with the most pheromone = best solution!
