import itertools

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def total_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        distance += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    distance += euclidean_distance(cities[route[-1]], cities[route[0]])  # Kembali ke kota awal
    return distance

def greedy_tsp(cities):
    num_cities = len(cities)
    all_routes = list(itertools.permutations(range(num_cities)))

    min_distance = float('inf')
    best_route = None

    for route in all_routes:
        distance = total_distance(route, cities)
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance

# Koordinat kota
cities = {
    1: (2, 5), 2: (8, 3), 3: (6, 9), 4: (4, 7),
    5: (10, 2), 6: (12, 6), 7: (3, 10), 8: (9, 8),
    9: (5, 4), 10: (11, 1), 11: (7, 12), 12: (1, 9),
    13: (10, 5), 14: (4, 3), 15: (8, 11), 16: (6, 1),
    17: (3, 7), 18: (9, 4), 19: (12, 10), 20: (2, 2)
}

# Cari rute dan jarak minimum
best_route, min_distance = greedy_tsp(cities)

# Tampilkan hasil
print("Rute Terbaik:", best_route)
print("Jarak Minimum:", min_distance)

#%%
