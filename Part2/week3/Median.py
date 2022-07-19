import os 
import sys 
from Heap import H_high, H_low

def balance(heap_high, heap_low):
    if heap_low.length >= heap_high.length and heap_low.length - heap_high.length <= 1:
        return 
    
    while heap_low.length - heap_high.length > 1:
        temp = heap_low.extract_max()
        heap_high.insert(temp)
    while heap_low.length < heap_high.length:
        temp = heap_high.extract_min()
        heap_low.insert(temp)
    return


def main(file):
    heap_high = H_high()
    heap_low = H_low()
    res = 0
    with open(file) as f:
        for num in f.readlines():
            if num:
                num = int(num)
                if not heap_high.heap:
                    heap_low.insert(num)
                elif num > heap_high.heap[0]:
                    heap_high.insert(num)
                else:
                    heap_low.insert(num)
                balance(heap_high, heap_low)
                # print(heap_low.heap, heap_high.heap)
                res += heap_low.heap[0] % 10000
    
    return res % 10000



if __name__ == '__main__':
    py_path = sys.argv[0]
    py_dir = os.path.dirname(py_path)
    filename = "Median.txt"
    filepath = os.path.join(py_dir, filename)
    print(main(filepath))