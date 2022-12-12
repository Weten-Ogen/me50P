def mygen():
    yield 1
    yield 2
    yield 3

g = mygen()

# print(value)


f = sorted(g)


def countdown(n):
    print("Starting")
    while n > 0:
        yield n
        n -= 1

cd = countdown(10)

val = next(cd)

def fibonacci(n):
    a,b = 0, 1
    while a < n :
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))


