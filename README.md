# Computer-Science-Publication-Similarity

# Algorithmic Methods of Data Mining

### Authors:
* Biko Catalano
* Andrea Marcocchia
* Malick Alexandre Ngorovitch Sarr

#### The folder  contains:

- **load_save**:  file.py some functions to save, load and read the following format: json, pickle and graph

- **Part_1**:     file.py, process and create graph

- **Part_2_A**:   file.py, subgraph induced by conference in input, some centralities measures

- **Part_2_B**:   file.py, Hop Distance of subgraph induced

- **Part_3_A**:   file.py, Evaluate dijkstra distance from a starting node

- **Part_3_B**:   file.py, GroupNumbers of a subset of nodes

- **building_output**:   file.py, built a nice output, using previous modules

- **main_code**:  file.ipynb, run building_output.py and give the output in a notebook format

- **report**: file.pdf, extensively comment the results obtained


# Analyze modules

## load_save.py

A module that contains functions to load, save json and pickle and to save and read graph. In input is requested the path of the file without file extension.


The file are called in this way:


```python
def load_json(name):
    with open(name + '.json', 'r') as f:
        return json.load(f)
```

## Part_1.py

We create a class, **parsejson_graph**. This module provides, when called, to create a dictionary and a graph.
It takes in input the json file.
This class has the following methods:

- **jaccard_sim**

    This function computes the jaccard similarity between two nodes.


- **dict_name**
   
   this function creates a dictionary that has the author_id as keys, and as values a nested dictionary with the     following attributes:

     
     - author_name: name
     - id_publication_int: list of publication
     - id_conference_int: list of conference


- **graph_complete**

 This function build the graph. It use the dictionary created in dict_name function to give the attributes to nodes.


- **pub_id**

  This function provide to build a index of publications:

   - publication_id: values list of authors

  This index allows a faster creation of edges. Compute the combination among authors with the same publications.


- **add_weighted_edges**

 Add weighted edges to graph. We use the *itertools.combinations* to find all the combinations of linked authors.
 This functions provides to weight the nodes using the function **jaccard_sim**.



## part_2_A.py


This module contains:
   
- **class Part_2_a**  
    
    this class take in input a conference_id, the dictionary and the graph. It builds the subgraph induced and compute some centralities measure.
   
In this module, there are also:
- 3 functions: plot the previous centralities measure (degree, betweenness and closeness)
    
- 1 function that plots correlation measures and prints correlation values in a table


## part_2_B.py

This module contains:
   
 - **class Part_2_b**: 
 
    This class has 3 methods:
     
    * **author_neighbors**: it searchs and return a list of all neighbours of a node 
         
    * **hop_distance**: Compute all neighbours at given distance d and compute induced subgraph. Originally, we had found the methods ego_graph, but we have seen it was very slow, so we prefer build the function ex-novo, using only the methods nx.all_neighbors(graph,node). Iterating this method  we have found all edges linked to starting node at distance d, given in input. We used this list of edges to build the subgraph.
         
    * **draw_author_subgraph**:draw the induced subgraph, obtained in the previous function. The input node is blue in the plot, all the others are red.


##  part_3_A


This module contains two functions:
   
 - **weight_dict**: create a dictionary that contains for each node of the graph all the linked nodes and their weigths. It ask in input only the graph. This function returns a dictionary.
 
 - **dijkstra_heap2**: return for a node in input (start) the shortest path for all the nodes that have path with the starting one. This function asks in input a starting node and the dictionary obtained in the previous function. The return is a dictionary.

##  part_3_B

This module contains only one function:
* **group_number**: this function return a dictionary with authors_ID of the subset as keys, and for values the node that have for GroupNumber that key. The requested input is the subset of nodes, the dictionary obtained in part_3_A with function weight_dict and the graph.

##  building_output

This module contains six functions that organize the output for all the modules already analyzed:
* **Part_1**
* **Part_2_A**
* **Part_2_B**
* **Part_3_A**
* **Part_3_A_solution**
* **Part_3_B**

# How to run the code

Open Jupyter notebook and run main_code.ipynb.

The output is in .ipynb file, in order to obtain clear results and plots, following the homework questions.

It is necessary to save the database (.json file) in the same directory in which are stored the other modules. In other case is necessary to write the full path.

The code works by default with **full_dbpl stored in the same directory**. If you want to change the database or the path, you have to change the argument of building_output.Part_1(*new argument*), in main_code.ipynb.

The homework questions are at the following link: http://aris.me/contents/teaching/data-mining-ds-2017/homeworks/homework4.pdf
