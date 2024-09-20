
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node)  
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            print(node)  
            visited.add(node)
            
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

print("DFS Recursive:")
dfs(graph, 'A')

print("\nDFS Iterative:")
dfs_iterative(graph, 'A')
