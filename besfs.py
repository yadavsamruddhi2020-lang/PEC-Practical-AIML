import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = []

    # (heuristic value, node)
    heapq.heappush(priority_queue, (heuristic[start], start))

    while priority_queue:
        h, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal found!")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    print("\nGoal not found!")


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (estimated distance to goal F)
heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 3,
    'F': 0
}

print("Best-First Search:")
best_first_search(graph, 'A', 'F', heuristic)