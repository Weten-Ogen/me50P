class Empty(Exception):
    pass

class stack:
    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return len(self._data) == 0

    def __repr__(self):
        return f"{self._data}"
    def top(self):
        if self.is_empty():
            pass
        else: 
            top = self._data[-1]
        return top
    
    def push(self, e):
        self._data.append(e)
    
    def pop(self):
        if self.is_empty():
            pass
        else:
            pop = self._data.pop()
        return pop
    
    def height(self):
        return len(self._data)
    
if __name__ == "__main__":
    stack()