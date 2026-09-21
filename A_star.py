def a_star(graph, h, start, goal):
    open_list = [start]
    g = {start: 0}
    parent = {start: None}

    while open_list:
        # Select node with minimum f = g + h
        current = min(open_list, key=lambda x: g[x] + h[x])

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        open_list.remove(current)

        for neighbor, cost in graph[current]:
            new_g = g[current] + cost

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                parent[neighbor] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None


# Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'G': []
}

# Heuristic values
h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'G': 0
}

start = 'A'
goal = 'G'

path = a_star(graph, h, start, goal)

print("Shortest Path:", path)