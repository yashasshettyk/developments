class QueueADT:
    def __init__(self):
        self.data = []
    
    def enqueue(self,e):
        self.data.insert(0,e)
        return self.data
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            self.data.pop()
            return self.data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.data[-1]
    
    def size(self):
        return len(self.data)
        
    def is_empty(self):
        return len(self.data)==0
            
        
s1 = QueueADT()
s1.enqueue("a")          
s1.enqueue("q")          
s1.enqueue("b")
print(s1.enqueue("Z"))          
print(s1.dequeue()) 
print(s1.size())
print(s1.is_empty())         
    
