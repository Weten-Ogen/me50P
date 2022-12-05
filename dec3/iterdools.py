import itertools



# Product
a = [1,3]
b = [2,5]
prod = itertools.product(a, b)
print(f"Products : {list(prod)}")

# Permutations
c = [1,3,5]
perm = itertools.permutations(c)
print(f"Permutations : {list(perm)}")

# Combinations
d = [1,10,11]
comb = itertools.combinations(d,2)
comb_rep = itertools.combinations_with_replacement(d, 2)
print(f"Combinations : {list(comb)}")
print(f"Combinations_with_rep: {list(comb_rep)}")


# Accumulators
e = [1,2,3,4]

acc = itertools.accumulate(e)

print(f"Accumulators: {list(acc)}")

# Groupby
f = [6,7,8,9]
groupObj = itertools.groupby(f, key=lambda x : x < 8 )
for key, values in groupObj:
    print(f"Groupby : {key} {list(values)} ")

# Infinite Iterators
# Count
for i in itertools.count(10):
    print(f"Infinite Count : {i}")
    if i == 16:
        break

# Cycle
g = [1,2,3]
for i in itertools.cycle(g):
    print(f"Infinite Cycle : {i}")
    if i == 3:
        break

# Repeat 
for i in itertools.repeat(1,4):
    print(f"Infinite Repeat : {i}")
    