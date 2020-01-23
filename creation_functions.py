from pynode.main import *
import pickle

highest_id = 0
edges_are_directed = False

def save(filename,*args,**kwargs):
    data = graph.nodes()+graph.edges()
    data = [node for node in data if not node.attribute('special')]
    pickle.dump(data,open(filename,'wb'))
    print('Saved!')

def undo(history,*args,**kwargs):
    global highest_id
    if not history.empty():
        last_creation = history.get()
        #i know remove_all looks like a weird decision
        #but it's the only type agnostic way to remove something
        graph.remove_all([last_creation])
        if type(last_creation) == Node:
            highest_id -= 1

def directed_toggle(this_node,*args,**kwargs):
    global edges_are_directed
    edges_are_directed ^= True
    if edges_are_directed:
        graph.add_edge(this_node,this_node)
    else:
        toggle_edge = this_node.incident_edges()[0]
        graph.remove_edge(toggle_edge)

def create_edge(selected,new_selection,*args,**kwargs):
    global edges_are_directed
    new_edge = Edge(
        selected,
        new_selection,
        directed=edges_are_directed
    )
    graph.add_edge(new_edge)
    selected.set_color(Color.DARK_GREY)
    return new_edge

def create_node(history,*args,**kwargs):
    global highest_id
    new_node = Node(highest_id+1)
    highest_id +=1
    new_node.set_attribute('special',False)
    graph.add_node(new_node)
    history.put(new_node)
