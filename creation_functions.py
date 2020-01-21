from pynode.main import *
import pickle

def save():
    data = graph.nodes()+graph.edges()
    data = [node for node in data if not node.attribute('special')]
    pickle.dump(data,open('graph.g','wb'))
    print('Saved!')

def create_edge(selected,new_selection):
    #otherwise create the edge
    print(selected,new_selection)
    graph.add_edge(Edge(selected,new_selection))
    selected.set_color(Color.DARK_GREY)

def create_node():
    new_node = Node()
    new_node.set_attribute('special',False)
    graph.add_node(new_node)