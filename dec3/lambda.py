from functools import reduce

add10 = lambda x : x + 10
mullp = lambda x, y : x * y 

# Sorted
arr = [(3,3),(4,2),(6,4), (5,8)]
arr_sort = sorted(arr, key=lambda x: x[1])
arr_sort2 = sorted(arr)
arr_sort3 = sorted(arr, key = lambda x: x[0] + x[1])

# Map
arr1 = [1,2,3,4,5]
sam = map(lambda x : x * 2, arr1)

# List comprehension
sam1 = [x*2 for x in arr1]
soul1 = [x  for x in arr1 if x % 2 == 0]

# Filter
soul = filter(lambda x : x % 2 == 0, arr1)

# Reduce
product = reduce(lambda x , y : x * y , arr1)

# Prints
print(f"add10 : { add10(5)}")
print(f"mullp : {mullp(5,2)}")
print(f"Sorted_second: {arr_sort}" )
print(f"Sorted_arr : {arr_sort2}" )
print(f"Sorted_sum : {arr_sort3}")
print(f"Map_sam: {list(sam)}")
print(f"List_Com : {sam1}")
print(f"Filter_soul: {list(soul)}")
print(f"ListComp_soul { list(soul1)}")
print(f"Reduce_product: {product}")