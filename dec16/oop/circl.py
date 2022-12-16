class Circle:
    pi =3.14

    def set_val (self):
        self.radius = int(input("Enter a number : "))
    
    def area(self):
        print("Area is : ", Circle.pi * self.radius ** 2)

    def circum(self):
        print("Circumference is : " , 2 * Circle.pi * self.radius)

c = Circle()

c.set_val()
c.area()
c.circum()
