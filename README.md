# graphical-graphs
 A GUI for making graphs in pynode.

## About the tool

#### What does it do?

graphical-graphs is a tool for making graphs in pynode because doing it by hand is *super* tedious. It provides a native way to make and share graphs that doesn't require typing it all out by hand. After all, isn't pynode designed to make these things easier?

#### How do I use it?

1. (Optional) Install pynode if you don't already have it. This repo comes with a version of it already but it isn't guaranteed to work on all platforms.
4. Run `creator.py`
4. To add a node, click the yellow "create_node" button
5. To select a node, just click on it.
6. To create an edge between two nodes, first select a node and then click on another node. 
7. To undo a step, click the red "undo" node
7. To toggle directed edges, click the black "directed" button. If it's turned on, the node will have an edge that connects it to itself.
8. When you're done, click on the green button labeled "save". The graph will be saved as a python pickle file.
9. To use the graph again in another program, add the following code to the top of the run function:
```python
#load graph
data = pickle.load(open('graph.g','rb'))
graph.add_all(data)
```

​		Also remember to add an `import pickle` at the top of your file.

## Upcoming features:

* ~~Dynamically adding nodes~~ *Done!*
* ~~Directed edges~~ *Done!*
* ~~Undo button~~ *Done!*
* (Maybe) Redo button
* (Maybe) Node deletion button that isn't undo

If you have any other ideas for features tell me and I'll add them, or, feel free to make a pull request!
