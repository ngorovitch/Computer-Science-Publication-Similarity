import networkx as nx
import json
import collections
from collections import Counter
import itertools
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pickle
from load_save import load_json
from load_save import save_obj_pickle
from load_save import save_graph



class parsejson_graph:
    '''Define a clas to build a dictionary, a graph and add to the graph the weighted edges'''
    
    def __init__(self,json):
       
       self.data=json
       self.dictionary=self.dict_name(self.data)
       self.graph=self.graph_complete(self.dictionary)
       self.inverse_pub= self.pub_id(self.data)
       self.add_weighted_edges= self.add_weighted_edges(self.inverse_pub,self.graph)
        
    
    def jaccard_sim(self,set1,set2):
        '''Ask in input two list of publication and return the Jaccard similarity between them'''
        
        set1=set(set1)
        set2=set(set2)
        
        return len(set1 & set2)/len( set1 | set2)
        
    
    
    
    def dict_name(self,data):
            '''Return a dictionary that has like keys the author_id, and values a nested dictionary with all attributes:
             - author_name: name
             - id_publication_int: list of publication
             - id_conference_int: list of conference'''
            
            DICT={}
              # Iterate on the every record of the dataset in input
            for i in tqdm(range(len(data))):
            
            
                for auth in range(len(data[i]['authors'])):
                
                # Evaluate if the author is already in the dict, if not, add is ID as key and after add conference and publication
                    if data[i]['authors'][auth]['author_id'] not in DICT.keys():
                   
                        DICT[data[i]['authors'][auth]['author_id']]={'author_name':data[i]['authors'][auth]['author'],
                                                       'id_publication_int':[data[i]['id_publication_int']],
                                                       'id_conference_int':[data[i]['id_conference_int']]}    
                 
                # If the author is already in the dict, append a new value (conference and pubblication)
                    else:
                        DICT[data[i]['authors'][auth]['author_id']]['id_publication_int'].append(data[i]['id_publication_int']),
                        DICT[data[i]['authors'][auth]['author_id']]['id_conference_int'].append(data[i]['id_conference_int'])    
                       
                                     
            return DICT           
                    
    
                
    def graph_complete(self,data):
        
        '''Return the graph with all the nodes'''
        
        print('building  graph and node...')  
        
        G=nx.Graph()
        for k,v in tqdm(data.items()):
            
            #**v take the dict like attr
            G.add_node(k, **v)  
        return G
    
    
    
    
    def pub_id(self,data):
        '''Return index publication, using the dataset in input '''
        
        print('building  index publications...')
        
        # Inizialize an empty dictionary
        dict_publication={}
        
        for i in tqdm(range(len(data))):
            dict_publication[data[i]["id_publication_int"]]=[]
            
            # Iterate on authors
            for j in range(len(data[i]["authors"])):
                dict_publication[data[i]["id_publication_int"]].append(data[i]["authors"][j]["author_id"]) 
            
                        
        return dict_publication
    
    
    
       
            
    def add_weighted_edges(self,pub,graph):
        '''Add weighted nodes to graph. '''
        
        print('adding weighted nodes...')
    
        for p in tqdm(pub.keys()):
            
            # use the itertools.combinations to find the linked authors.
            for (i,v) in itertools.combinations(pub[p], 2):
            
                graph.add_edge(i,v, weight= 1-self.jaccard_sim(graph.node[i]['id_publication_int'],
                                                          graph.node[v]['id_publication_int']))
 






    