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