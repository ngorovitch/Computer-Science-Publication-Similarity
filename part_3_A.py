# Import modules
import networkx as nx
import json
import collections
from collections import Counter,defaultdict
import itertools
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pickle
import numpy  as np
from sklearn.cluster import KMeans
import seaborn as sns
import load_save
from load_save import read_graph
from heapq import *



def weight_dict(graph):
    '''Create a dictionary that contains for each node of the graph all the linked nodes and their weigths'''

    # Define the list where will be stored data
    lst_tot=[]
    for xx in tqdm(graph.nodes()): 
        for yy in graph[xx]:
            # Save the weigth between node xx and node yy
            lst=(xx,yy,graph[xx][yy]["weight"])
            lst_tot.append(lst)
        
    # Store the information obtained previously in a dictionary       
    g = defaultdict(list)

    for node1,node2,weight in tqdm(lst_tot):
        g[node1].append((weight,node2))    
    
    return g     

def dijkstra_heap2(g, start):
    '''Create a function that return for a node in input (start) the shortest path for all the nodes that have path with the starting one'''
    maw = {}
    # Inizialize q
    q = [(0,start)] 
    # Inizialize the seen variable empty. It will be update with the seen nodes
    seen=set()
    while q:
        # Pop the smaller element of q
        (cost,v1) = heappop(q)
        
        # If the selected node is not already seen, we will execute the following commands
        if v1 not in seen:
            # Add the current node to the seen
            seen.add(v1)
            # For node v1 get all the neighbour
            for c, v2 in g.get(v1, ()):
                
                # Check if v2 is not an already seen node
                if v2 not in seen:
                    
                    
                    heappush(q, (cost+c, v2))
            maw[v1] = cost
    return (maw)



