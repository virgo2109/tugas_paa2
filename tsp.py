import itertools

def tsp_brute_force(graph, start):
    # Mencari semua permutasi kemungkinan rute
    nodes = list(graph.keys())
    nodes.remove(start)
    permutations = list(itertools.permutations(nodes))

    # Inisialisasi variabel terbaik dengan nilai tak terhingga
    best_distance = float('inf')
    best_route = None

    # Menghitung jarak total untuk setiap rute dan memperbarui rute terbaik
    for permutation in permutations:
        current_route = [start] + list(permutation) + [start]
        current_distance = 0

        for i in range(len(current_route) - 1):
            current_distance += graph[current_route[i]][current_route[i + 1]]

        if current_distance < best_distance:
            best_distance = current_distance
            best_route = current_route

    return best_route, best_distance

# Contoh penggunaan
graph = {
    'A': {'A': 0, 'B': 2, 'C': 9, 'D': 6},
    'B': {'A': 1, 'B': 0, 'C': 4, 'D': 2},
    'C': {'A': 6, 'B': 3, 'C': 0, 'D': 7},
    'D': {'A': 3, 'B': 6, 'C': 8, 'D': 0}
}
start_node = 'A'

best_route, best_distance = tsp_brute_force(graph, start_node)
print("Rute terbaik:", best_route)
print("Jarak terbaik:", best_distance)
