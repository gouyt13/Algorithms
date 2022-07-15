import collections
import sys
import os



def createGraph(filename):
    edges = []
    for l in open(filename):
        fields = [int(f) for f in l.split()]
        edges.append(tuple(fields))

    graph = collections.defaultdict(list)
    reversed_graph = collections.defaultdict(list)
    for e in edges:
        graph[e[0]] = graph[e[0]] + [e]
        reversed_graph[e[1]] = reversed_graph[e[1]] + [(e[1], e[0])]

    return graph, reversed_graph, edges


t = 0
s = 0
finishing = {}
leader = {}
explored = collections.defaultdict(int)


def paraReset():
    global t, s, finishing, leader, explored
    t = 0
    s = 0
    finishing = {}
    leader = {}
    explored = collections.defaultdict(int)


def DFSLoop(labeling, reversed=False):
    global s
    global explored
    for i in labeling:
        if not explored[i]:
            s = i
            DFS(i, reversed)


forward_graph = {}
reversed_graph = {}


def DFS(start, reversed=False):
    global t
    global reversed_graph
    global forward_graph
    global leader 
    if reversed:
        graph = reversed_graph
    else:
        graph = forward_graph
    

    # Iterative (i.e. manually managing a stack) solution.
    stack = []
    stack.append((start, 1))

    while len(stack) > 0:
        current, phase = stack.pop()
        if phase == 1:
            explored[current] = 1
            leader[current] = s
            edge_found = False
            for edge in graph[current]:
                if not explored[edge[1]]:
                    stack.append((current, 1))
                    stack.append((edge[1], 1))
                    edge_found = True
                    break
            if not edge_found:
                stack.append((current, 2))
        if phase == 2:
            t += 1
            finishing[current] = t
    return 


py_path = sys.argv[0]
py_dir = os.path.dirname(py_path)
filename = "SCC.txt"
filepath = os.path.join(py_dir, filename)
forward_graph, reversed_graph, edges = createGraph(filepath)

print("Graph created")

num_nodes = 875714
labeling = range(num_nodes, 0, -1)
DFSLoop(labeling, True)

print("Reverse DFSLoop done")

inverse_finishing = dict((v, k) for k, v in finishing.items())
finish_labeling = [inverse_finishing[i] for i in range(num_nodes, 0, -1)]

paraReset()
DFSLoop(finish_labeling)

print("Forward DFSLoop done")

sccs = {}
for i in leader:
    if leader[i] not in sccs:
        sccs[leader[i]] = [i]
    else:
        sccs[leader[i]].append(i)


a = [len(sccs[i]) for i in sccs]
a.sort(reverse=True)
print(a[:5])