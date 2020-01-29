from pynode.main import *
from creation_functions import *
import pickle
import queue

#globals
filename = 'graph.g'
selected = None
history = queue.LifoQueue()
special_nodes = {
    'save':{
        'function':save,
        'colour':Color.GREEN
    },
    'create':{
        'function':create_node,
        'colour':Color.YELLOW
    },
    'undo':{
        'function':undo,
        'colour':Color.RED
    },
    'directed':{
        'function':directed_toggle,
        'colour':Color.BLACK
    }
}

def on_click(new_selection):
    global selected,special,history,filename
    if new_selection.id() in special_nodes.keys():
        return special_nodes[new_selection.id()]['function'](
            history=history,
            this_node=new_selection,
            filename=filename
        )
    if not selected:
        selected = new_selection
        new_selection.set_color(Color.BLUE)
    else:
        new_edge = create_edge(selected,new_selection)
        history.put(new_edge)
        selected = None

def run():
    offset = 0.1
    #dynamically sets the starting position of the nodes
    current_x = (1-(offset*len(special_nodes)))/2
    for name,details in special_nodes.items():
        node = Node(id=name)
        node.set_color(details['colour'])
        node.set_attribute('special',True)
        node.set_position(current_x,0.5,relative=True)
        current_x += offset
        graph.add_node(node)

register_click_listener(on_click)
begin_pynode(run)