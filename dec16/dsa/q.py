class circularq:
    """
        This is a circular queue implementation in python
        :k : represent the capacity of the queue
        :queue : is the list containing the elements
        :head : is the first item to be added to the queue 
        :tail : is also points to the first item to be added to the list 
    """

    def __init__(self, k):
        self.k = k 
        self.queue = [None] * k
        self.head = self.tail = -1
       

    def enqueue(self, data):
        if (self.tail + 1) % self.k == self.head:
            old = self.queue
            self.k *= 2 
            new = []  * self.k
            print(old)
            new = [*old,*new]
            self.queue = new
            print(f"new q: {self.queue}")
            print(f'resized the array')

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data

        else: 
            self.tail = (self.tail  + 1) % self.k
            self.queue[self.tail] = data

    

    def dequeue(self):
        if self.head == -1:
            print('the Q is empty ')

        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp 
        
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp
        


q = circularq(6)
q.enqueue(5)
print(f'\n*****Queue******\n{q.queue}\n')
q.enqueue(6)
print(f'\n*****Queue******\n{q.queue}\n')
q.enqueue(200)
