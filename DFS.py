def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            for neighbor in range(len(graph[node]) - 1, -1, -1):
                if graph[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
