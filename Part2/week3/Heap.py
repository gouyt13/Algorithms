class H_low():
    """
    root value is the maximun of the heap
    """
    def __init__(self) -> None:
        self.heap = []
        self.length = 0

    def bubble_up(self, index):
        p = (index+1)//2-1
        if index == 0 or self.heap[index] <= self.heap[p]:
            return 
        self.heap[index], self.heap[p] = self.heap[p],  self.heap[index]
        self.bubble_up(p)

    def bubble_down(self, index):
        t = index * 2 + 1
        if t >= self.length:
            return 
        if t + 1 < self.length and self.heap[t+1] > self.heap[t]:
            t = t + 1
        
        if self.heap[index] < self.heap[t]:
            self.heap[index], self.heap[t] = self.heap[t], self.heap[index]
            self.bubble_down(t)
        return 
            
    def insert(self, num):
        self.heap.append(num)
        self.length += 1
        self.bubble_up(self.length-1)
    
    def extract_max(self):
        res = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.length -= 1
        if self.length > 1:
            self.bubble_down(0)
        return res 

    

class H_high():
    def __init__(self) -> None:
        self.heap = []
        self.length = 0

    def bubble_up(self, index):
        p = (index+1)//2-1
        if index == 0 or self.heap[index] >= self.heap[p]:
            return 
        self.heap[index], self.heap[p] = self.heap[p],  self.heap[index]
        self.bubble_up(p)

    def bubble_down(self, index):
        t = index * 2 + 1
        if t >= self.length:
            return 
        if t + 1 < self.length and self.heap[t+1] < self.heap[t]:
            t = t + 1
        
        if self.heap[index] > self.heap[t]:
            self.heap[index], self.heap[t] = self.heap[t], self.heap[index]
            self.bubble_down(t)
        return 
            
    def insert(self, num):
        self.heap.append(num)
        self.length += 1
        self.bubble_up(self.length-1)
    
    def extract_min(self):
        res = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.length -= 1
        if self.length > 1:
            self.bubble_down(0)
        return res 