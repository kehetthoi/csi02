graph = {
    0:[1,4],
    1:[0,2,3,4],
    2:[1,3],
    3:[1,2,4],
    4:[0,1,3]
}
def is_connected(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == end:
        return True
    for neighbor in graph[start]:
        if neighbor not in visited:  
            if is_connected(graph, neighbor, end, visited):  
                return True
    return False
print(is_connected(graph,0,3))  
