import  heapq
k = [1000,40,0,5450,60]
print(heapq.nlargest(3,k))
print(heapq.nsmallest(3,k))
m = list(k)
heapq.heapify(m)
print(m)
