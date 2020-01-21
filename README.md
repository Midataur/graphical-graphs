# graphical-graphs
 A GUI for making graphs in pynode.

##About the tool

####What does it do?

graphical-graphs is a tool for making graphs in pynode because doing it by hand is *super* tedious. It provides a native way to make and share graphs that doesn't require typing it all out by hand. After all, isn't pynode designed to make these things easier?

####How do I use it?

1. (Optional) Install pynode if you don't already have it. This repo comes with a version of it already but it isn't guaranteed to work on all platforms.
2. Open `creator.py`
3. Specify the number of nodes you want in the `node_num` variable in the `creator.py` source. Dynamic addition of nodes will be added soon.
4. Run `creator.py`
5. To select a node, just click on it.
6. To create an edge between two nodes, first select a node and then click on another node. Be careful as there isn't currently an easy way to undo edge creation.
7. When you're done, click on the green node labeled "save". The graph will be saved as a python pickle file.
8. To use the graph again in another program, add the following code to the top of the run function:
```python
#load graph
data = pickle.load(open('maze.g','rb'))
graph.add_all(data)
```

​		Also remember to add an `import pickle` at the top of your file.

## Upcoming features:

* Dynamically adding nodes
* Directed edges
* Undo button
* (Maybe) Node deletion button

If you have any other ideas for features tell me and I'll add them, or, feel free to make a pull request!