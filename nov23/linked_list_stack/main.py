class Empty(Exception):
    pass



class LinkedStack:

    class _Node:
        def __init__(self,element,next):
            self._element = element
            self._next = next

    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0 

    def push(self, e):
        self.head = self._Node(e,self.head)
        self.size += 1 

    def top(self):
        if self.is_empty():
            return 
        else:
            return self.head._element
    
    def __str__(self):
        return f"{self.head._element}"
    
    def pop(self):
        top  = self.head._element
        self.head = self.head._next
        self.size -= 1
        return top
    


T = LinkedStack()
T.push(5)

T.push(6)

print(T.pop())
print(T)
