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

def has_eulerian_cycle(A):
    return all(degree_sequence(A) % 2 == 0)

def connect_vertices(A, i, j):
    A[i][j] = A[j][i] = 1

def disconnect_vertices(A, i, j):
    A[i][j] = A[j][i] = 0

def find_vertices_with_odd_degrees(degrees):
    return [i for i, degree in enumerate(degrees) if degree % 2 != 0]

def make_eulerian(A):
    while not has_eulerian_cycle(A):
        degrees = degree_sequence(A)
        odd_vertices = find_vertices_with_odd_degrees(degrees)
        v1, v2 = random.sample(odd_vertices, 2)
        if not A[v1][v2]:
            connect_vertices(A, v1, v2)
        else:
            common_neighbors = [v for v in range(len(A)) if A[v1][v] and A[v2][v]]
            if common_neighbors:
                neighbor = random.choice(common_neighbors)
                disconnect_vertices(A, v1, neighbor)
                disconnect_vertices(A, v2, neighbor)
            else:
                disconnect_vertices(A, v1, v2)
    return A

def create_graph_file(A,filename):
    array = A.tolist()
    i = 0
    j = 0
    file = open(filename, "w")
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

def genAndFix(n,p):

    #Create initial graph and save it to file
    A = generate_graph(n, p)
    print("Initial graph:")
    print(A)

    create_graph_file(A,"Initial_graph.txt")

    #Modify graph to be Eulerian and save it to file
    A = make_eulerian(A)
    print("Eulerian graph:")
    print(A)

    create_graph_file(A,"Eulerian_graph.txt")

    




