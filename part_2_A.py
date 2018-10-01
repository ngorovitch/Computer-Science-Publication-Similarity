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
import seaborn as sns
import load_save
import pandas as pd


class Part_2_a:
    '''take in input a conference_id , the dictionary the graph and build the subgraph induced and compute some centralities measure'''
    
    def __init__(self,Dict,conf_id,graph):
         
         
        self.graph=graph
        self.Dict=Dict
        self.conf_id=conf_id
        self.conference_subgraph= self.conference_subgraph(self.Dict,self.conf_id,self.graph)
         
     
        
    def conference_subgraph(self,data,conf_id,graph):
        '''Return the subgraph induced by the set of authors who published at least once at the input conference'''
        
        
        return graph.subgraph([k for k in tqdm(data.keys()) if conf_id in data[k]['id_conference_int']])

    
    def draw_subgraph(self):
         
        nx.draw(self.conference_subgraph,with_labels=False,node_size=2,edge_color='grey', width = 0.1,font_weight='bold')
        plt.show()
                        
    
    def degree(self):
        '''Evaluate the degree centrality in the subgraph in input'''
        return nx.degree_centrality(self.conference_subgraph)
    
    
    def closeness(self):
        '''Evaluate the closeness centrality in the subgraph in input'''
        return nx.closeness_centrality(self.conference_subgraph)

     
    def betweeness(self):
        '''Evaluate the betweenness centrality in the subgraph in input'''
        return nx.betweenness_centrality(self.conference_subgraph)
         
            
     

         
def plot_degree_centrality(degree_centrality):

    sns.distplot( degree_centrality, hist=True, kde=True, rug=False)
    plt.show()
    
def plot_closeness(closeness):
    
    sns.distplot(closeness, hist=True, kde=True, rug=False,color='orange')
    plt.show()

def plot_betweeness(betweeness):
    
    sns.distplot( betweeness, hist=True, kde=True, rug=False,color='green')
    plt.show()

    
def correlation(df):
    '''use library seaborn to show a correlation plot'''
    sns.pairplot(df, vars=['closeness','betweeness','degree_centrality'], kind='reg')
    plt.show()
    print(df.corr(method='pearson', min_periods=1))
    