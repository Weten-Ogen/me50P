arr = ["v", "k", "a","c", "f"]
# arr.sort()
arr.remove('k')
print(arr)

list_org = ["banana", "apples", "cherry"]
list_cpy = list_org.copy()

list_cpy.append('mango')
print(f"{list_org}\n", list_cpy)

newbot = [x for x in range(10)]
print(newbot)

# Tuples
anc = ("max", 3 , "box") 
print(anc)

tag = anc
print(tag.count('max'))

# Dict 
mydict = {
    "name": "Max",
    "age" : 28,
    "city" : "Boston",
}

mydict2 = dict(name="max", age="28", city="Boston", email="marcuso@harvard.edu")
mydict.update(mydict2)
print(mydict)

ditc = {1:}