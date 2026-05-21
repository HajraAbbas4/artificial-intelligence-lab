# ---------------- Experiment 1 ----------------
# Heuristic Search Strategy: A* Search

import heapq


def a_star_search(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))
    visited = set()

    while open_list:
        f_cost, g_cost, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g_cost

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g_cost = g_cost + cost
                new_f_cost = new_g_cost + heuristics[neighbor]
                heapq.heappush(open_list, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))

    return None, float("inf")


graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 3)],
    "D": [("G", 1)],
    "E": [("G", 2)],
    "F": [("G", 2)],
    "G": [],
}

heuristics = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 2,
    "E": 3,
    "F": 2,
    "G": 0,
}

path, cost = a_star_search(graph, heuristics, "A", "G")
print("Experiment 1: A* Search")
print("Path:", path)
print("Total Cost:", cost)
