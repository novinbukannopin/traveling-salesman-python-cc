import numpy as np

from greedy import euclidean_distance


class Cuckoo:
    def __init__(self, solution, fitness):
        self.solution = solution
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
        cuckoo = Cuckoo(solution, fitness)
        population.append(cuckoo)
    return population

def levy_flight(beta=1.5):
    sigma_u = (np.math.gamma(1 + beta) * np.sin(np.pi * beta / 2) / np.math.gamma((1 + beta) / 2) * beta * 2**((beta - 1) / 2))**(1 / beta)
    u = np.random.normal(0, sigma_u)
    v = np.random.normal(0, 1)
    step = u / abs(v)**(1 / beta)
    return step

def cuckoo_search_tsp(cities, population_size, generations):
    population = initialize_population(population_size, cities)

    for generation in range(generations):
        # Sort population by fitness in ascending order
        population.sort(key=lambda cuckoo: cuckoo.fitness)

        # Generate new solutions using Levy flights
        new_population = []
        for cuckoo in population:
            step_size = levy_flight()
            new_solution = generate_random_solution(cities)
            for i in range(len(new_solution)):
                if np.random.rand() < step_size:
                    j = np.random.randint(len(new_solution))
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_fitness = calculate_total_distance(new_solution, cities)
            new_cuckoo = Cuckoo(new_solution, new_fitness)
            new_population.append(new_cuckoo)

        # Combine old and new solutions, keep the best
        combined_population = population + new_population
        combined_population.sort(key=lambda cuckoo: cuckoo.fitness)
        population = combined_population[:population_size]

    best_cuckoo = min(population, key=lambda cuckoo: cuckoo.fitness)
    best_solution = best_cuckoo.solution
    best_distance = best_cuckoo.fitness

    return best_solution, best_distance

# Koordinat kota
cities = {
    1: (2, 5), 2: (8, 3), 3: (6, 9), 4: (4, 7),
    5: (10, 2), 6: (12, 6), 7: (3, 10), 8: (9, 8),
    9: (5, 4), 10: (11, 1), 11: (7, 12), 12: (1, 9),
    13: (10, 5), 14: (4, 3), 15: (8, 11), 16: (6, 1),
    17: (3, 7), 18: (9, 4), 19: (12, 10), 20: (2, 2)
}

# Parameter Cuckoo Search
population_size = 50
generations = 100

# Cari rute dengan Cuckoo Search
cuckoo_route, cuckoo_distance = cuckoo_search_tsp(cities, population_size, generations)

# Tampilkan hasil Cuckoo Search
print("Rute Terbaik (Cuckoo Search):", cuckoo_route)
print("Jarak Total (Cuckoo Search):", cuckoo_distance)
