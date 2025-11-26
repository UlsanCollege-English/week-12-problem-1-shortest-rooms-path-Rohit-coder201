from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Missing start or goal → no path
    if start not in graph or goal not in graph:
        return []

    # Start equals goal → path is just [start]
    if start == goal:
        return [start]

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                # Stop early if goal found
                if neighbor == goal:
                    path = []
                    while neighbor is not None:
                        path.append(neighbor)
                        neighbor = parent[neighbor]
                    return path[::-1]

    return []  # No path exists
