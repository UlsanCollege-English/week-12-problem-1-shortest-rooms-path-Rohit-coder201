from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Missing start or goal
    if start not in graph or goal not in graph:
        return []

    # Start == goal
    if start == goal:
        return [start]

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

                if neighbor == goal:
                    # Rebuild path
                    path = []
                    cur = goal
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    return path[::-1]  # reverse path

    return []  # No path
