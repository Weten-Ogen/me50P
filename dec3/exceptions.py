x = 2
if x < 1:
    raise Exception("This showed be more than 1")

assert(x > 1), 'x is positive'

try: 
    x = 5/ 1
except ZeroDivisionError:
    print('number can not be divided by zero')

class ValueHigh(Exception):
    pass

def kmean(x):
    if x > 5:
        raise ValueHigh('Reduce the number')
    
try:
    kmean(200)
except ValueHigh as e:
    print(e)