class Sample:
    __val = 10

    def set_val(self):
        self.__val = 20
    
    def get_val(self):
        print("Class val : " , Sample.__val)
        print("Instance val : ", self.__val)
        

obj = Sample()
obj.set_val()
obj.get_val()


print(obj.__val)