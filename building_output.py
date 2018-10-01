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
from load_save import load_json, save_obj_pickle,save_graph,load_obj_pickle
from  Part_1  import parsejson_graph
from part_2_A import Part_2_a
from part_2_B import Part_2_b
import  part_2_A
import  part_2_B
import part_3_A
import part_3_B
import pandas as pd



def Part_1(json):                   
        
        print('loading data...')
        
        data= load_json(json)         
        P=parsejson_graph(data)      #parse json and building graph
        
        # If you want to save the objects, remove the code comment
        
        #print('Saving dictionary...')
        
        
        #save_obj_pickle(P.dictionary,'dict_'+json) 
        
          
        
        Author_Graph=P.graph
        
        #print('Saving Graph...')
        
        #save_graph(Author_Graph,'Graph_'+json)
          
          
        print('info Graph... ')
        
        print( nx.info(Author_Graph)) 
                    
        
        return P.dictionary,Author_Graph
    

def Part_2_A(Dict,Graph):
            
            conf_list={v  for k in tqdm(Dict.keys()) for v in Dict[k]['id_conference_int']}
            control=False
            while control==False:
                    
                print("Insert conference id:")
                conf_input=int(input())
        
                
                if conf_input not in conf_list:
                
                        print("ERROR\nConference ID not found")
                        print("Try another time")
                        print("\n")
            
                else:
                        control=True
             
            print('building conference subgraph...')    
            
            c=Part_2_a(Dict,conf_input,Graph)
            sub_graph=c.conference_subgraph
            
            print('subgraph info...')
            
            print( nx.info(sub_graph)) 
            
            print('check number of nodes...type yes if you want the plot ')
            
            if str(input())=='yes':
                
    
                print('drawing graph...')
                c.draw_subgraph()
            
            else:
                
                pass
            
            print('computing degree_centrality...')
            
            degree_centrality=c.degree()
            
            
            print('computing closeness...very slow full_data')
            
            closeness=c.closeness()
            
            print('computing betweeness...very slow full_data...')
            
            betweeness=c.betweeness()
            
            print('...end')
            
            
            data_frame=pd.DataFrame({'closeness':list(closeness.values()),
                    'betweeness':list(betweeness.values()),
                    'degree_centrality':list(degree_centrality.values())})
      
            
            
            return degree_centrality,closeness,betweeness,sub_graph, data_frame


def Part_2_B(Dict,Graph):
    
            control=False
            while control==False:
                    
                print("Insert author id:")
                author_id=int(input())
        
                
                if author_id not in Dict.keys():
                
                        print("ERROR\n author_id not found")
                        print("Try another time")
                        print("\n")
            
                else:
                        control=True
                        
            P= Part_2_b()            
            
            print('insert hop_distance d:')
            
            d= int(input()) 
            
            print('computing Hop Distance...')
            
            Hop_Distance_subgraph=P.hop_distance(Graph,author_id,d)
            
            print('subgraph info...')
            
            print( nx.info(Hop_Distance_subgraph)) 
            
            print('check number of nodes... plot the graph type yes ')
            
            if str(input())=='yes':
                
    
                print('drawing graph...')
            
                P.draw_author_subgraph()
    
            return Hop_Distance_subgraph

def Part_3_A(starting_graph):

    return part_3_A.weight_dict(starting_graph)

def Part_3_A_solution(def_dict,starting_graph):  
    
     
    control=False
    while control==False:
        print("Type author id:")
        aut_input=int(input())
        if aut_input in starting_graph.nodes():
            control=True
        else:
            print("Invalid input:\nTry another time\n")
    
    aris=256176
    aux = part_3_A.dijkstra_heap2(def_dict,aris)
    
    if aut_input in aux.keys():
        print(aux[aut_input])
    else:
        print("There is no possible path")

def Part_3_B(D_dict,graph):
    
    subset=[]
    controll=False
    while controll==False:
        sub_set_n=int(input("Insert the number of nodes that you want to insert in the subset:"))
        if sub_set_n>21:
            print("Cardinality has to be smaller that 21!")
        else:
            controll=True
    for i in range(sub_set_n):
        cont=False
        while cont==False:
            print("Insert element number",i+1)
            element=int(input())
            if element not in graph.nodes():
                print("This node is not in the graph!\n Insert another time the",i+1,"node")
            elif element in subset:
                print("This element has already been selected")
            else:
                subset.append(element)
                cont=True
    
    
    
    return part_3_B.group_number(subset,D_dict,graph)

