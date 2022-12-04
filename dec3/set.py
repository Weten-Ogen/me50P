setis = set()
setis.add(1)
setis.add(10)
setis.add('name')
setis.add(False)
setis.add(1)
# print(setis)

# for i in setis:
   

# if 'name' in setis:
#     print('sexism')


# Union
odd = {1,3,5,7,9}
even = {2,4,6,8}
primes = {2,3,5,7}

inter = odd.union(even)
unoora = odd.intersection(primes)
dff = even.difference(odd)
sym_dff = even.symmetric_difference(odd)

setA = {1,3,45,6, 56}
setb = {100,101,102,103}

odd.update(setA)
even.intersection_update(setA)
primes.difference_update(setA)
setb.symmetric_difference_update(setA)


# will not modify the original set
print(f"Union : {inter}")
print(f"Intersection : {unoora}")
print(f"Difference: {dff}")
print(f"Symmetric_Diff: {sym_dff}")

# modify set in places
print(f"Update: {odd}")
print(f"Intersection_update: {even}")
print(f"Difference_update: {primes}")
print(f"Symmetric_update: {setb}")

