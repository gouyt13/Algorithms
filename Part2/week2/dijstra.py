import os 
import sys 
from collections import defaultdict


num_nodes = 200 
res = {i:1000000 for i in range(1, 201)}; res[1] = 0
X = set(); X.add(1)
V = set(range(1, 201))

def create_graph(filename):
    edges = defaultdict(dict)

    with open(filename) as f:
        for line in f.readlines():
            tmp = line.strip().split()
            tile = int(tmp[0])
            for i in tmp[1:]:
                head, length = i.split(',')
                head, length = int(head), int(length)
                edges[tile][head] = length

    return edges 

def main(edges):
    global num_nodes, res, X, V
    while X != V:
        tmp = 1000000
        w = 1
        for v in X:
            for cur,length in edges[v].items():
                if cur not in X and length + res[v] < tmp:
                    tmp = length + res[v]
                    w = cur 
        res[w] = tmp 
        X.add(w)

        


if __name__ == '__main__':
    py_path = sys.argv[0]
    py_dir = os.path.dirname(py_path)
    filename = "dijstraData.txt"
    filepath = os.path.join(py_dir, filename)
    edges = create_graph(filepath)
    main(edges)
    
    answer = [res[i] for i in [7,37,59,82,99,115,133,165,188,197]]
    print(answer)