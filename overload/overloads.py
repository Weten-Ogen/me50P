class User():
    def __init__(self, name):
        self.name =name

    def __repr__(self):
        return 'Instance {} is of  class User'.format(self.name)


m = User("Xavier")
print(m)