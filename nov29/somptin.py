class Compton:
    def __init__(self):
        self.data = []
    
    def past(self, e):
        self.data.append(e)
    
    def __bool__(self):
         return bool(self.data)
    

C = Compton()


if C:
    print("yes")
else:
    print("NO")