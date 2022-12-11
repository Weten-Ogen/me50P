import random 

a = random.randint(1,10)
b = random.random()
c = random.uniform(1,10)
d = random.randrange(1,10)
e  = random.normalvariate(0,1)
arr = ['harry','luna','ron','hermione','neville','cho','draco','cedric','sheamus','dean','ginny']
f = random.choices(arr, k=5)
g = random.sample(arr ,5)
h = random.shuffle(arr)

# Destructure
print(f"randint : {a}")
print(f"random : {b}")
print(f"uniform : {c}")
print(f"randrange: {d}")
print(f"randvariate: {e}")
print("#############list random ############")
print(f"random choice : {f}")
print(f"random sample : {g}")
print(f"shuffle : {h}")