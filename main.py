from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Missing start or goal -> return empty path
    if start not in graph or goal not in graph:
        return []

    # Start equals goal -> single node path
    if start == goal:
        return [start]

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                if neighbor == goal:
                    # rebuild path from goal to start
                    path = []
                    cur = goal
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    return path[::-1]

    return []  # no path found
