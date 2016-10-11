#from graph_tool.all import *
import networkx as nx
import matplotlib.pyplot as plt
import time
import csv

COLORMAP_JAVA 	 = '0x73e600'
COLORMAP_PYTHON  = '0x00c7ff'
COLORMAP_C 		 = '0xff336a'
COLORMAP_USER 	 = '0xffe7e0'
COLORMAP_OTHER	 = '0xffe7e0'
COLORMAP_DEFAULT = '0xffffff'

class graph:
	G = nx.Graph()
	layoutType = 'spring'
	layout = None
	nodes = dict()

	def __init__(self, nodes, edges):
		for node in nodes:
			if not self.nodes.has_key(node[0]):
				self.nodes[node[0]] = node[1]
			self.G.add_node(node[0], nodeType=node[1])
		for edge in edges:
			self.G.add_edge(edge[0], edge[1], edgeType=edge[2])

	def printInfo(self):
		print 'The graph has {} nodes, edges'.format( self.G.number_of_nodes(), self.G.number_of_edges() )

	def display(self):
		nx.draw(self.G, pos=self.layout)
		plt.show()

	def layout(self, layoutType='spring'):
		self.layoutType = layoutType
		if layoutType == 'spring':
			self.layout = nx.spring_layout(self.G)
		elif layoutType == 'spectral':
			self.layout = nx.spectral_layout(self.G)
		elif layoutType == 'shell':
			self.layout = nx.shell_layout(self.G)
		elif layoutType == 'random':
			self.layout = nx.random_layout(self.G)
		elif layoutType == 'circular':
			self.layout = nx.circular_layout(self.G)
		else:
			self.layout = nx.spring_layout(self.G)

	def getLayout(self):
		result = []
		for graphID in self.layout:
			color = COLORMAP_DEFAULT
			if graphID%2 == 0:
				color = COLORMAP_USER
			elif graphID%2 == 1:
				# if self.nodes[graphID].lower() == 'java'
				# 	color = COLORMAP_JAVA
				# elif self.nodes[graphID].lower() == 'python':
				# 	color = COLORMAP_PYTHON
				# elif self.nodes[graphID].lower() == 'c':
				# 	color = COLORMAP_C
				# else:
					color = COLORMAP_OTHER

			result.append({	'graphID':graphID, 
							'x': float(self.layout[graphID][0]), 'y': float(self.layout[graphID][1]), 'z': 0,
							'size': int(self.G.degree(graphID)**0.2), 'color': color})
		return result


#test
#nodes = [[1,'java'], [2,'other'], [3,'java'], [4,'c'], [5,'c'], [6,'python']]
#edges = [[1,2,1], [2,3,1], [3,1,1], [1,4,2], [2,5,2], [3,6,2]]
#g = graph(nodes, edges)
#g.layout('spring')
#print g.getLayout()

file_edge=open("D:\\VMware\\Compass-py\\file\\edge5000")
edge_list=[]
for line in file_edge.readlines():
	edge_line=line.strip('\n').split(' ')
	edge_line=map(eval,edge_line)
	edge_list.append(edge_line)
print edge_list
file_node=open("D:\\VMware\\Compass-py\\file\\node5000")
node_list=[]
for linen in file_node.readlines():
	node_line=linen.strip('\n').split(' ')
	node_line=map(eval,node_line)
	node_list.append(node_line)

print node_list
start = time.clock()

g1 = graph(node_list, edge_list)
g1.printInfo()
g1.layout('spring')

print g1.getLayout()
end = time.clock()
print end-start
#g1.display()

c=g1.getLayout()
# csvfile = file('D:\\VMware\\Compass-py\\file\\result.csv', 'wb')
# writer = csv.writer(csvfile)
# writer.writerow(['graphID', 'color', 'y', 'x', 'z', 'size'])
#
# writer.writerow()
# csvfile.close()
f=open('D:\\VMware\\Compass-py\\file\\result.csv', 'wb')
for nodelayout in g1.getLayout():
	print>>f,nodelayout
f.close()