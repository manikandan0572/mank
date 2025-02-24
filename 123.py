def dfs(graph, start):

    visited = set()
    traversal_order = []

    def dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return traversal_order


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
traversal_order = dfs(graph, start_node)
print(f"DFS traversal order starting from {start_node}: {traversal_order}")
