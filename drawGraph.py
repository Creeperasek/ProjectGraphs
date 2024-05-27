from pyvis.network import Network
import webcolors as color


#Drawing function - creates html file with drawn file
def draw_graph(filename,graphfile,n):
    g = Network()

    file = open(filename,"r")

    nodes = [0,1,2,3,4,5,6,7,8,9]
    g.add_nodes(nodes=nodes,
                label=["0","1","2","3","4","5","6","7","8","9"],
                color=[color.rgb_to_name((255,0,0)),# Red
                       color.rgb_to_name((0, 0, 255)), #Blue
                       color.rgb_to_name((0, 255, 0)), #Green
                       color.rgb_to_name((139, 0, 139)), # Magenta
                       color.rgb_to_name((0, 0, 0)), #Black
                       color.rgb_to_name((205, 133, 63)), #Peru
                       color.rgb_to_name((0, 139, 139)), #DarkCyan
                       color.rgb_to_name((139, 69, 19)), #Saddle Brown
                       color.rgb_to_name((46, 139, 87)), #SeaGreen
                       color.rgb_to_name((112, 128, 144)) #SlateGray
                       ])

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
