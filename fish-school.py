import numpy as np

from greedy import euclidean_distance


class Fish:
    def __init__(self, position, fitness):
        self.position = position
        self.fitness = fitness

def generate_random_solution(cities):
    solution = list(cities.keys())
    np.random.shuffle(solution)
    return solution

def calculate_total_distance(solution, cities):
    distance = 0
    for i in range(len(solution) - 1):
        distance += euclidean_distance(cities[solution[i]], cities[solution[i + 1]])
    distance += euclidean_distance(cities[solution[-1]], cities[solution[0]])  # Kembali ke kota awal
    return distance

def initialize_population(population_size, cities):
    population = []
    for _ in range(population_size):
        solution = generate_random_solution(cities)
        fitness = calculate_total_distance(solution, cities)
        fish = Fish(solution, fitness)
        population.append(fish)
    return population

def update_fish_position(current_position, step_size):
    new_position = current_position + step_size * np.random.uniform(-1, 1, len(current_position))
    return new_position

def search_behavior(current_position, step_size, cities):
    new_solution = generate_random_solution(cities)
    for i in range(len(new_solution)):
        if np.random.rand() < step_size:
            j = np.random.randint(len(new_solution))
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    new_fitness = calculate_total_distance(new_solution, cities)
    return new_solution, new_fitness

def fish_school_search_tsp(cities, population_size, generations):
    population = initialize_population(population_size, cities)
    step_size_initial = 0.1
    step_size_decay = 0.95

    for generation in range(generations):
        for fish in population:
            step_size = step_size_initial * step_size_decay**generation
            new_position = update_fish_position(fish.position, step_size)
            new_solution, new_fitness = search_behavior(fish.position, step_size, cities)

            if new_fitness < fish.fitness:
                fish.position = new_position
                fish.fitness = new_fitness
            else:
                fish.position = update_fish_position(fish.position, step_size / 2)

    best_fish = min(population, key=lambda fish: fish.fitness)
    best_solution = best_fish.position
    best_distance = best_fish.fitness

    return best_solution, best_distance

# Koordinat kota
cities = {
    1: (2, 5), 2: (8, 3), 3: (6, 9), 4: (4, 7),
    5: (10, 2), 6: (12, 6), 7: (3, 10), 8: (9, 8),
    9: (5, 4), 10: (11, 1), 11: (7, 12), 12: (1, 9),
    13: (10, 5), 14: (4, 3), 15: (8, 11), 16: (6, 1),
    17: (3, 7), 18: (9, 4), 19: (12, 10), 20: (2, 2)
}

# Parameter Fish School Search
population_size = 50
generations = 100

# Cari rute dengan Fish School Search
fish_route, fish_distance = fish_school_search_tsp(cities, population_size, generations)

# Tampilkan hasil Fish School Search
print("Rute Terbaik (Fish School Search):", fish_route)
print("Jarak Total (Fish School Search):", fish_distance)
