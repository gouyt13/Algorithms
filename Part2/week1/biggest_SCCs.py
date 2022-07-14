from heapq import heappop, heappush
from collections import defaultdict
import os 
import sys


NUM_NODES = 9 


def create_graph():
    """
    create graph and arc_reversed graph 
    """
    py_path = sys.argv[0]
    py_dir = os.path.dirname(py_path)
    filename = 'SCC.txt'
    filepath = os.path.join(py_dir, filename)

    # graph and arc-reversed graph
    graph = defaultdict(list)
    graph_rev = defaultdict(list)

    with open(filepath) as f:
        for line in f.readlines():
            if line:
                tail, head = line.strip().split()
                tail, head = int(tail), int(head)
                graph[tail-1].append(head)
                graph_rev[head-1].append(tail)
    return graph, graph_rev  


def DFS_Loop1(graph_rev):
    """
    the second step of Kosaraju's Two-Pass Algorithm
    calculate finishing times on the G-rev
    """
    t = 0
    node_flag = [False] * NUM_NODES
    finishing_time = dict()

    def DFS(graph_rev, i):
        nonlocal node_flag
        nonlocal finishing_time
        nonlocal t 
        node_flag[i-1] = True 
        for j in graph_rev[i-1]:
            if node_flag[j-1] == False:
                DFS(graph_rev, j)
        t += 1 
        # use t as key, more convenient to use graph 
        finishing_time[t] = i 
    
    for i in range(NUM_NODES, 0, -1):
        if node_flag[i-1] == False:
            DFS(graph_rev, i)
    
    # print(finishing_time)
    return finishing_time  


def DFS_Loop2(graph, finishing_time):
    """
    use finishing time to find SCCs on the graph 
    record the size of SCC
    """
    node_flag = [False] * NUM_NODES
    res = [0, 0, 0, 0, 0]

    def DFS(graph, i):
        nonlocal num 
        nonlocal node_flag
        node_flag[i-1] = True 
        for j in graph[i-1]:
            if node_flag[j-1] == False:
                DFS(graph, j)
        num += 1

    for i in range(NUM_NODES, 0, -1):
        node = finishing_time[i]
        num = 0 # the size of SCC 
        if node_flag[node-1] == False:
            DFS(graph, node)
        top5(res, num)

    return res 


def top5(res, cur):
    # use heap to record top 5 of the sizes 
    temp = heappop(res)
    if temp < cur:
        heappush(res, cur)
    else:
        heappush(res, temp)




if __name__ == '__main__':
    graph, graph_rev = create_graph()
    finishing_time = DFS_Loop1(graph_rev)
    res = DFS_Loop2(graph, finishing_time)
    print(sorted(res, reverse=True))