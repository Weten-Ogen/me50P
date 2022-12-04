from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque




#  Counter
a = "aaabbbbbccccdddd"
my_counter = Counter(a)
print(f"Counter : {my_counter.most_common()}")
print(f"Counter : {list(my_counter.elements())}")

# nametupe
Points = namedtuple('Points', 'x y')
pt = Points(1, -4)
print(f"Nametuple: {pt}")



# OrderedDict
dict_ord = OrderedDict()
dict_ord['a'] = 2
dict_ord['b'] = 30
dict_ord['c'] = 50
dict_ord['d'] = 24
dict_ord['e'] = 10

print(f"OrderedDict : {dict_ord}")

# DefaultDict
deefault = defaultdict(int)

deefault['a'] = 1
deefault['e'] = 50
deefault['b'] 

print(f"defaultDict : { deefault}")
b = deque()
b.append(1)
b.append(2)
b.append(50)
b.appendleft(60)
b.pop()
b.popleft()
b.extend([4,5,6])
b.extendleft([8,9, 10])
b.rotate(-1)


# Deque
print(f"Deque : {b}")