from stackify import stack

S = stack()
T = stack()
for e in range(10):
    S.push(e)


def recuss(a):
    if a.is_empty():
        return
    else:
        val = a.pop()
        return recuss(a)
    

recuss(S)
print(S)


def moving(a, b):
    print(f"Stack S : {a}")
    for i  in range(a.height()):
        j = a.pop()
        b.push(j)
    print(f"Stack T:{b}")


