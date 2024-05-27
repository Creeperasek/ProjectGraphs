import generateGraph
import drawGraph

nodes = 10
p = 0.7

generateGraph.genAndFix(nodes,p)

drawGraph.draw_graph("Initial_graph.txt","Initial_graph.html",nodes)
drawGraph.draw_graph("Eulerian_graph.txt","Eulerian_graph.html",nodes)