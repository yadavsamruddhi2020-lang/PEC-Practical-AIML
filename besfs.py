import heapq

def best_first(g, start, goal, h):
    q = [(h[start], start)]
    visited = set()

    while q:
        _, node = heapq.heappop(q)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            break

        for n in g[node]:
            if n not in visited:
                heapq.heappush(q, (h[n], n))

g = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

h = {'A':5, 'B':4, 'C':2, 'D':6, 'E':3, 'F':0}

best_first(g, 'A', 'F', h)
