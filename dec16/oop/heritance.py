class Person:
    def __init__(self):
        self.__first = None
        self.__last = None
        
        self.__address = None
        self.__tel  = 0

    def set_per(self):
        self.__first = input('Enter a firstname: ')
        self.__last  = input('Enter a surname: ')
      
        self.__address = input('Enter a address: ')
        self.__tel = input('Enter a tel no: ')
       
    def get_per(self):
        print(f"\nfirstName : {self.__first}\nSurname : {self.__last}\nAddress:{self.__address}:Tel no:  {self.__tel}")


per = Person()

class Employee(Person):
    def __init__(self):
        self.__id = 0
        self.__sal = 0

    def set_emp(self):
        self.__id =int(input("Enter a valid id: "))
        self.__sal =int(input('Enter your salary: '))
    
    def get_emp(self):
        print(f"ID: {self.__id}\nSalary: {self.__sal}")