class Nigaru():
    def __init__(self,name,house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.house} : {self.name}"
    
    def __add__(self, x):
        return self.name + x
    
x = Nigaru("Hermione","Gryffindor")
print(x + " oware")