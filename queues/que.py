class Empty(Exception):
    pass


class MyQueue:
    def __init__(self):
        self._data = []
    
    def __repr__(self):
        return f"Queue : {self._data}"

    def size(self):
        return self._size

    def first(self):
        first = self._data[0]
        self._data = self._data[1:]
        return first
    
    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            pass
        else:
            e = self._data[0]
            self._data = self._data[1: ]
            return e


if __name__ == "__main__":
    MyQueue()