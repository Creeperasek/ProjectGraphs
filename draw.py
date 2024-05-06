from pyvis.network import Network

#Number of nodes
n = 10

#Drawing function - creates html file with drawn file
def draw_graph(filename,graphfile):
    g = Network()

    file = open(filename,"r")

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
    print("Edges: "+ str(i)+"\n")
    print("Adjective list:")
    print(g.get_adj_list())

    D = (2 * i) / (n * (n - 1))
    print("\nGraph density = " + str(round(D,3)))

    #g.hrepulsion(node_distance=500)
    g.toggle_physics(True)
    g.barnes_hut()
    g.write_html(graphfile, True, False,False)

#Main
draw_graph("Initial_graph.txt","Initial_graph.html")
draw_graph("Eulerian_graph.txt","Eulerian_graph.html")