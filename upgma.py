import numpy as np
import Node

try:
	from ete3 import Tree, TreeStyle
except ImportError:
	print("Make sure you have the following packages installed: PyQt5, ete3")

class upgma:
	def __init__(self, matrix, nodesList):
		self.m = matrix
		self.nodesList = nodesList
		self.newickFormat = ""

	def findMinDist(self):
	    #return indices of 2nd minmum (because first minimum is 0)
	    mn =  np.min(np.partition(self.m, kth=1)[:,1])
	    return np.argwhere(self.m == mn)[0]


	def calcMatrix(self, i, j):
	  	#Calculate the new distances between the new node (fusionNode) and other element of the matrix.
	    l = len(self.m)
	    for x in range(j+1, l):
	        self.m[x][i] = self.m[i][x] = (self.m[i][x]+self.m[j][x])/2
	         
	    self.m = np.delete(self.m, j, axis=1)
	    self.m = np.delete(self.m, j, axis=0)
	    
	    return self.m


	def fusionNodes(self, rightNode, leftNode, dij):
	  fusionNode = Node.Node("")

	  fusionNode.rightNode = leftNode
	  fusionNode.leftNode = rightNode
	  fusionNode.rightDist = dij/2             #calculate the new right distance
	  fusionNode.leftDist = dij/2 - leftNode.rightDist  #Calculate The new Left Distance
	  fusionNode.id = "({} : {}, {} : {})".format(rightNode.id, str("%.5f " % fusionNode.rightDist), leftNode.id, str("%.5f " % fusionNode.rightDist))
	  
	  return fusionNode

	#Newick Format
	def newick(self):
		print(self.newickFormat)

	#Tree clustering
	def show(self):
		t = Tree(self.newickFormat+";")
		ts = TreeStyle(self.newickFormat+";")
		ts.show_leaf_name = True
		ts.show_branch_length = True
		ts.show_branch_support = True
		t.show(tree_style=ts)
		

	def algo(self):
		while len(self.m) != 1:
			[x,y] = self.findMinDist()
			#Create fusion Node
			f = self.fusionNodes(self.nodesList[x], self.nodesList[y], self.m[x][y])
			
			#Delete fusioned Nodes and add the new fusionNode 
			self.nodesList.pop(x)
			self.nodesList.insert(x, f)
			self.nodesList.pop(y)
			#Calculate New Distance Matrix
			self.calcMatrix(x,y)
		#Save Newick Format Text
		self.newickFormat = self.nodesList[0].id