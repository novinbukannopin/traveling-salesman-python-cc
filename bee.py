import numpy as np

from greedy import euclidean_distance


class Bee:
    def __init__(self, route, distance):
        self.route = route
        self.distance = distance

def generate_random_route(cities):
    route = list(cities.keys())
    np.random.shuffle(route)
    return route

def calculate_total_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        distance += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    distance += euclidean_distance(cities[route[-1]], cities[route[0]])  # Kembali ke kota awal
    return distance

def initialize_population(population_size, cities):
    population = []
    for _ in range(population_size):
        route = generate_random_route(cities)
        distance = calculate_total_distance(route, cities)
        bee = Bee(route, distance)
        population.append(bee)
    return population

def select_best_bees(population, elite_size):
    population.sort(key=lambda bee: bee.distance)
    return population[:elite_size]

def scout_bees(population_size, cities):
    scouts = initialize_population(population_size, cities)
    return scouts

def generate_neighbor_bee(existing_bee):
    route = existing_bee.route.copy()
    i, j = np.random.choice(len(route), size=2, replace=False)
    route[i], route[j] = route[j], route[i]
    distance = calculate_total_distance(route, cities)
    return Bee(route, distance)

def employed_bee_phase(employed_bees, cities):
    new_population = []
    for bee in employed_bees:
        neighbor_bee = generate_neighbor_bee(bee)
        if neighbor_bee.distance < bee.distance:
            new_population.append(neighbor_bee)
        else:
            new_population.append(bee)
    return new_population

def onlooker_bee_phase(employed_bees, onlooker_bees, cities):
    probabilities = [1 / bee.distance for bee in employed_bees]
    probabilities /= np.sum(probabilities)

    new_population = []
    for _ in range(len(onlooker_bees)):
        selected_index = np.random.choice(len(employed_bees), p=probabilities)
        selected_bee = employed_bees[selected_index]
        neighbor_bee = generate_neighbor_bee(selected_bee)
        new_population.append(neighbor_bee)

    return new_population

def bee_algorithm_tsp(cities, population_size, generations):
    employed_bees = initialize_population(population_size, cities)
    onlooker_bees = scout_bees(population_size, cities)
    elite_size = int(0.1 * population_size)

    for generation in range(generations):
        employed_bees = employed_bee_phase(employed_bees, cities)
        best_employed_bees = select_best_bees(employed_bees, elite_size)
        onlooker_bees = onlooker_bee_phase(best_employed_bees, onlooker_bees, cities)

    best_bees = select_best_bees(employed_bees + onlooker_bees, 1)
    best_route = best_bees[0].route
    best_distance = best_bees[0].distance
    return best_route, best_distance

# Koordinat kota
cities = {
    1: (2, 5), 2: (8, 3), 3: (6, 9), 4: (4, 7),
    5: (10, 2), 6: (12, 6), 7: (3, 10), 8: (9, 8),
    9: (5, 4), 10: (11, 1), 11: (7, 12), 12: (1, 9),
    13: (10, 5), 14: (4, 3), 15: (8, 11), 16: (6, 1),
    17: (3, 7), 18: (9, 4), 19: (12, 10), 20: (2, 2)
}

# Parameter Bee Algorithm
population_size = 50
generations = 100

# Cari rute dengan Bee Algorithm
bee_route, bee_distance = bee_algorithm_tsp(cities, population_size, generations)

# Tampilkan hasil Bee Algorithm
print("Rute Terbaik (Bee Algorithm):", bee_route)
print("Jarak Total (Bee Algorithm):", bee_distance)
