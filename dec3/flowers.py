import functools

def deco_func(f):
    @functools.wraps(f)
    def wrapper(*args,**kwargs):
        print('Calculating... ')
        result = f (*args, **kwargs)
        print('Done')
        return result
    return wrapper


@deco_func
def nami(x):
    return x + 5

result = nami(10)
 
def repeat_n(num):
    def deco(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(5):
                result = f(*args, **kwargs)
            return result
        return wrapper
    return deco


@repeat_n(5)
def greet(name):
    print(f"Hello {name}")


greet('Marcus')

