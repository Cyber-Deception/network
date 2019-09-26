from networkx import nx
import os
import os.path as op
from inspect import stack

path_app = op.dirname(op.abspath(stack()[0][1]))
path_graphs = op.join(path_app, 'dataset')

for file in os.listdir(op.join(path_app, 'dataset')):
     try:
        graph = nx.read_gml(op.join(path_graphs, file))
     except nx.exception.NetworkXError:
        continue
     print(str(file)+' Nodes:'+ str(len(graph.nodes))+ ' Edges:'+ str(len(graph.edges)))

