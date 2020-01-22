from pynode.main import *
from creation_functions import *
import pickle
import queue

#globals
selected = None
history = queue.LifoQueue()
special_nodes = {
    'save':{
        'function':save,
        'colour':Color.GREEN
    },
    'create_node':{
        'function':create_node,
        'colour':Color.YELLOW
    },
    'undo':{
        'function':undo,
        'colour':Color.RED
    }
}

def on_click(new_selection):
    global selected,special,history
    if new_selection.id() in special_nodes.keys():
        return special_nodes[new_selection.id()]['function'](history=history)
    if not selected:
        selected = new_selection
        new_selection.set_color(Color.BLUE)
    else:
        new_edge = create_edge(selected,new_selection)
        history.put(new_edge)
        selected = None

def run():
    for name,details in special_nodes.items():
        node = Node(id=name)
        node.set_color(details['colour'])
        node.set_attribute('special',True)
        graph.add_node(node)

register_click_listener(on_click)
begin_pynode(run)
