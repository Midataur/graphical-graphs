from pynode.main import *
import pickle
import random
import math

first = None

def on_click(node):
    global first
    #handle saving
    if node == save:
        data = graph.nodes()+graph.edges()
        data.remove(save)
        pickle.dump(data,open('graph.g','wb'))
        print('Saved!')
        return None
    #see if we already have a node saved
    if not first:
        first = node
        first.set_color(Color.BLUE)
        return None
    #otherwise create the edge
    graph.add_edge(Edge(first,node))
    first.set_color(Color.DARK_GREY)
    first = None

def run():
    global save
    #add the amount of nodes we want
    nodenum = 4
    nodes = [Node(x,x) for x in range(nodenum)]
    graph.add_all(nodes)
    #create the save button
    save = Node(id='save',value='save')
    save.set_color(Color.GREEN)
    graph.add_node(save)

register_click_listener(on_click)
begin_pynode(run)
