import pickle
import json
import networkx as nx


def load_json(name):
    with open(name + '.json', 'r') as f:
        return json.load(f)


def load_obj_pickle(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def save_obj_pickle(obj, name):
    with open(name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)  


def save_graph(graph,file):
    
    return nx.write_gpickle(graph, file + 'gpickle')
    


def read_graph(file):   
    
    return nx.read_gpickle(file + 'gpickle')    
    