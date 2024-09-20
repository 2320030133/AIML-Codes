from collections import deque

# BFS function
def bfs(graph, start):
    visited = set()          
    queue = deque([start])    
    visited.add(start)        

    while queue:
        node = queue.popleft() 
        print(node, end=" ")   
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)  
                visited.add(neighbor)   

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  
