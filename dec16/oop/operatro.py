class Complex:
    def __init__(self):
        self.real = 0
        self.img = 0

    def set_val(self):
        self.real = int(input("Enter a real numbr : "))
        self.img = int(input("Enter an imaginary numbr: "))
    
    def __add__(self, other):
        temp= Complex()
        temp.real = self.real + other.real
        temp.img = self.img + other.img
        return temp
    
    def __str__(self):
        return f"{self.real} + {self.img}j"
  
    

obj1 = Complex()
obj2 =Complex()
obj1.set_val()
obj2.set_val()


obj = obj1 + obj2
print(obj)
