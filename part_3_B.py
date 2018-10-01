
# coding: utf-8

# In[ ]:


import pickle
import numpy  as np
from sklearn.cluster import KMeans
import seaborn as sns
import load_save
from load_save import read_graph
from heapq import *
import part_3_A
from tqdm import tqdm


def group_number(subset,D_dict,graph):
    '''Return a dictionary with authors ID of the subset as keys, and for values the node that have for GroupNumber that key'''
    
    groupNumbers = {}
    paths= {}
    cc=0
    for e in subset:
        
        # Modify the ID of author, adding sub before
        # It is necessary because it's better work with keys of the dict as string
        strings = 'sub'+str(e)
        
        # Csll the dijkistra function for each node in the subset
        paths[strings]=  part_3_A.dijkstra_heap2(D_dict,e)
        
        # Initialize groupNumbers in position string with an empty list
        groupNumbers[strings] = []
        
    # Iterate on each node of the graph in input
    for node in tqdm(graph):
        
        # mini is an auxiliar variable
        mini= []
        # Put mini is a heap data stracture
        heapify(mini)
        
        # Iterate on each node in the subgraph
        for path in paths.keys():
            
            # Evaluate if the node has a distance with the node (path) of the subgraph
            # If the node is not in paths[path].keys(), it means that there is no path between node and path
            if node in paths[path].keys():
                heappush(mini,(paths[path][node], path))
                
        # len(mini) is bigger than 0 if at least one of the subgraph node has path with the node
        # node is the one of the iteration in the graph
        if len(mini)>0:
            number= heappop(mini)
            
            groupNumbers[number[1]].append(node)

    return groupNumbers

