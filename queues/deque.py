from que import MyQueue
class Deque(MyQueue):
    def add_first(self,e):
        """
            :e -> takes an argument 
            insert to infront of the queue
        """
        self._data.insert(e)

    