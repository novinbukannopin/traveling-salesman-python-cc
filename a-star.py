import numpy as np

from greedy import total_distance


class Node:
    def __init__(self, city, parent=None):
        self.city = city
        self.parent = parent
        self.g = 0  # cost from start node to current node
        self.h = 0  # heuristic cost from current node to goal node
        self.f = 0  # total cost: f = g + h

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def a_star_tsp(cities):
    start_city = next(iter(cities))
    start_node = Node(city=start_city)
    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = min(open_set, key=lambda node: node.f)
        open_set.remove(current_node)
        closed_set.add(current_node.city)

        if len(closed_set) == len(cities):
            # All cities visited, construct the route
            route = []
            while current_node:
                route.insert(0, current_node.city)
                current_node = current_node.parent
            return route

        for neighbor_city in cities.keys():
            if neighbor_city not in closed_set:
                neighbor_node = Node(city=neighbor_city, parent=current_node)
                neighbor_node.g = current_node.g + euclidean_distance(cities[current_node.city], cities[neighbor_city])
                neighbor_node.h = euclidean_distance(cities[neighbor_city], cities[start_city])
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if neighbor_node not in open_set:
                    open_set.append(neighbor_node)

    return None

# Koordinat kota
cities = {
    1: (2, 5), 2: (8, 3), 3: (6, 9), 4: (4, 7),
    5: (10, 2), 6: (12, 6), 7: (3, 10), 8: (9, 8),
    9: (5, 4), 10: (11, 1), 11: (7, 12), 12: (1, 9),
    13: (10, 5), 14: (4, 3), 15: (8, 11), 16: (6, 1),
    17: (3, 7), 18: (9, 4), 19: (12, 10), 20: (2, 2)
}

# Cari rute dengan algoritma A*
a_star_route = a_star_tsp(cities)

# Hitung total jarak
a_star_distance = total_distance(a_star_route, cities)

# Tampilkan hasil A*
print("Rute Terbaik (A*):", a_star_route)
print("Jarak Total (A*):", a_star_distance)
