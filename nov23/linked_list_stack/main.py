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
