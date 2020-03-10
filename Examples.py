import numpy as np
import Node
import upgma

#==================== Example 1 =======================
m = np.array( [[0, 0.092, 0.106, 0.177, 0.207],
    [0.092, 0, 0.111, 0.193, 0.218], 
    [0.106, 0.111, 0, 0.188, 0.218], 
    [0.177, 0.193, 0.188, 0, 0.219], 
    [0.207, 0.218, 0.218, 0.219, 0]])

#Tree Nodes
A = Node.Node("Homme")
B = Node.Node("Chimpanze")
C = Node.Node("Gorille")
D = Node.Node("Orang-outan")
E = Node.Node("Gibbon") 
 
#List of Tree Nodes
nodesList = [A, B, C, D, E]

u = upgma.upgma(m, nodesList)

u.algo()
u.newick()

try:
	u.show()
except:
	print("Install PyQt5, ete3")

#====================== Example 2 ===============================#
m = np.array( [[0,9,2,4,9,10],
				[9,0,9,6,2,10],
				[2,9,0,5,9,10],
				[9,6,5,0,6,10],
				[9,2,9,6,0,10],
				[10,10,10,10,10,0]])

A = Node.Node("A")
B = Node.Node("B")
C = Node.Node("C")
D = Node.Node("D")
E = Node.Node("E") 
F = Node.Node("F")
 
#List of Tree Nodes
nodesList = [A, B, C, D, E, F]

u = upgma.upgma(m, nodesList)
u.algo()
u.newick()
try:
	u.show()
except:
	print("Install PyQt5, ete3")