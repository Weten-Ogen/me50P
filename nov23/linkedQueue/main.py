def main():
    t = LinkedQ()
    t.enqueue(5)
    t.enqueue(6)
    print(t)

class LinkedQ:
    class _Node():
        def __init__(self,element,next):
            self.element = element
            self.next = next
    
    
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def Size(self):
        return self.size
    
    def first(self):
        return self.tail.element
    
            
    
    def dequeue(self):
        if self.is_empty():
            pass
        ans =  self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self._tail = None
        return ans
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1
        

if __name__ == "__main__":
    main()

       
    
