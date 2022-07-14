"""
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6^{th}6 
th
  row looks like : "6	155	56	52	120	......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut.  (HINT: Note that you'll have to figure out an implementation of edge contractions.  Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.  But you should also think about more efficient implementations.)   (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.)  Write your numeric answer in the space provided.  So e.g., if your answer is 5, just type 5 in the space provided.
"""

import random
from copy import deepcopy


def createGraph(filename):
    with open(filename) as f:
        graph = {}
        for line in f.readlines():
            data = line.strip().split()
            graph[data[0]] = data[1:]

    return graph


def randomChoose(graph):
    node1 = random.choice(list(graph.keys()))
    node2 = random.choice(list(graph[node1]))
    return node1, node2


def karger(graph):
    while len(graph) > 2:
        node1, node2 = randomChoose(graph)
        graph[node1].extend(graph[node2])
        for n in graph[node2]:  # merge 2 node into 1 node
            graph[n].remove(node2)
            graph[n].append(node1)
        while node1 in graph[node1]:
            graph[node1].remove(node1)
        del graph[node2]

    min_cut = len(graph[node1])
    return min_cut


if __name__ == "__main__":
    graph = createGraph("kargerMinCut.txt")
    res = float("inf")
    for _ in range(1000):
        res = min(res, karger(deepcopy(graph)))

    print(res)
