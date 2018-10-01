import networkx as nx
import json
import collections
from collections import Counter
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




class Part_2_b:
    
    def __init__(self):
        
        self.Hop_Distance_graph=None
        self.node_input=None
        self.graph=None
        
        
    def author_neighbors(self,graph,n):
        '''Search all neighbours of a node'''
        return list(nx.all_neighbors(graph,n))
       
    
    def hop_distance(self,graph,node,d):
        '''Compute all neighbours at given distance d and compute induced subgraph'''
        
        self.node_input=node
        self.graph=graph
        
        # If distance is 0, return the starting node
        if d==0:
            
              self.Hop_Distance=node
              
              return self.node_input
        
        # If distance is equal to 1, return only the starting node neighbors
        elif d==1:
            
            self.Hop_Distance=self.author_neighbors(graph,node)+[node]
            
            return self.author_neighbors(graph,node)+[node]
         
        # In all the other cases:
        else:
            
            # ToT is set where will be added all the authors reached
            ToT=set([node])
            
            # N at the beginning are the neighbors of the author in input, N will be update in the for loop
            N=set(self.author_neighbors(graph,node))
            
            for i in range(d-1):
                
                # C is a set that is recalled empty every iteration of i
                C=set()
                
                # Iterate on the neighbors
                for n in N:
                    
                    # Search all neighbours of node n
                    L=self.author_neighbors(graph,n)
                    A=set(L)
                    C.update(A)
                    ToT.update(A)
                N=C
             
            # Create a subgraph from the list of found nodes
            self.Hop_Distance_graph=self.graph.subgraph(list(ToT)) 
            
            return self.Hop_Distance_graph
        
    def draw_author_subgraph(self):
         
        a=self.Hop_Distance_graph    
        set_color=[ 'blue' if node==self.node_input else 'red' for node in a]
        nx.draw(a, with_labels=False,node_color=set_color, node_size=2,edge_color='grey', 
                        width = 0.1,font_weight='bold')
        plt.show()
           
            
        
        
    





       