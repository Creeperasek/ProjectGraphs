from pyvis.network import Network

g = Network()

file = open("graph.txt","r")

nodes = [0,1,2,3,4,5,6,7,8,9]
g.add_nodes(nodes=nodes,
            label=["0","1","2","3","4","5","6","7","8","9"],
            color=["red","blue","green","brown","yellow","pink","purple","black","orange","dark_green"])

j = 0
i= 0

for node in range(9):
    line = file.readline()
    line = line[:10]
    edge=0
    
    for num in line:
        if(edge >= j):

            if(int(num) == 1):
                g.add_edge(node,edge)
        edge=edge+1
    
    j=j+1


i=0
for _ in g.get_edges():
    i=i+1
print(i)


print(g.get_adj_list())




g.hrepulsion(node_distance=500)
g.toggle_physics(True)
g.show('mygraph.html', True, False)