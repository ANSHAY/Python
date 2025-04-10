# /*
# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.
# */


def allPaths(graph, paths, currPath, start, end):
    if start == end:
        paths.append(currPath)        
        return
    for i in graph[start]:
        allPaths(graph, paths, currPath+[i], i, end)

paths = []
graph= {0:[1,2,3], 1:[3,5], 2:[4,5], 3:[4,5], 4:[5]}
allPaths(graph, paths, [0], 0, 5)        
print(paths)
            

    