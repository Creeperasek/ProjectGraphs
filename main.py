import numpy as np
import random
from collections import deque

def generate_graph(n, p):
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                A[i][j] = A[j][i] = 1
    return A

def degree_sequence(A):
    return np.sum(A, axis=1)

def order_odd_degrees(degrees):
    odd_degrees = [(i, degree) for i, degree in enumerate(degrees) if degree % 2 != 0]
    odd_degrees.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in odd_degrees]

def connect_vertices(A, i, j):
    A[i][j] = A[j][i] = 1

def bfs_connected_component(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(range(len(graph[vertex]))) - visited)
    
    return visited

def is_connected(graph):
    visited = bfs_connected_component(graph, 0)
    return len(visited) == len(graph)

def make_eulerian(A):
    if not is_connected(A):
        print("Graph is not connected. Making the graph connected first.")
        # Connect the graph before making it Eulerian
        # This is a simple way to connect the graph. You might need a more complex logic depending on the graph.
        for i in range(len(A) - 1):
            connect_vertices(A, i, i + 1)
    
    degrees = degree_sequence(A)
    odd_vertices = order_odd_degrees(degrees)
    
    while len(odd_vertices) > 1:
        v1 = odd_vertices.pop()
        v2 = odd_vertices.pop()
        connect_vertices(A, v1, v2)
    
    return A

n = 10  # przykładowy rozmiar grafu
p = 0.7  # przykładowe prawdopodobieństwo

A = generate_graph(n, p)
print("Initial graph:")
print(A)

if is_connected(A):
    print("The graph is connected.")
    A = make_eulerian(A)
    print("Eulerian graph:")
    print(A)

    
    array = A.tolist()

    i = 0
    j = 0

    file = open("graph.txt", "w")
    for line in array:
        j=j+1
        deg = 0
        
        for val in line:
            
            file.write(str(val))
            deg += val
            i = i + 1

            if(j==n and i==n):
                file.write(f"| {str(deg)}")
                continue
            elif(i == n):
                file.write(f"| {str(deg)}")
                file.write("\n")
                i = 0
                
    file.close()
    print('File Created Succesfuly')

else:
    print("The graph is not connected and cannot be made Eulerian.")




