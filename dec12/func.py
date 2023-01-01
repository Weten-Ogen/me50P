def your(name):
    print(f"your name {name}")




number = 10

def print_numb():
    number = 3 
    print(number)

def add(x):
    x = 5

n = 10 


if __name__ == "__main__":
    print("global & local value")
    print(f"Before number is {number}")
    print_numb()
    print(f"After number is {number}")
    print('\n  \n')
    print('called by refrence(in python: is called by object /obj refrence)')
    print(f"immutable val : {n}")
    add(10)
    print(f'can not be change : {n}')

