import secrets

a = secrets.randbelow(10)
b = secrets.randbits(4)
arr = ['Marcu', 'bittt']
c = secrets.choice(arr)
print(f"randbelow : {a}")
print(f"randbits : {b}")
print(f"choice : {c}")