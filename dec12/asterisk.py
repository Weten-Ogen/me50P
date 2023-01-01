# the operation of * operators in python
a = 5 * 7
b = 5 ** 2
c = [None, 0 ,2 ,4] * 4
d = "Marcus" * 2
e = (0, 1) * 3
#Use it to denot a keyword args
def man(a,b , c):
    return a, b ,c

import copy
f = [0 , 4, 5]
*g, l = f
k = f 
k[0] = 9

m = copy.copy(f)
m[0] = 9

n = [[1,2,3], [4,5,6]]
i = copy.copy(n)
i[0][0] = [7,8,9]
j = copy.deepcopy(n)




if __name__ == "__main__":
    print(f'basic mul  : {a}')
    print(f"exponential :  {b}")
    print(f"list tuple :  {c}")
    print(f"string multiple :  {d}")
    print(f"tuple  :  {e}")
    print(f"man function : {man(1,2,'marcus')}")
    print(f"args unpacking :  {man(*f)}")
    print(f" many & one unpackin :  {g} \n {l}")
    print(f"Shallow copyin :  \n{f}\n{k}")
    f = [0, 4,5]
    print(f"Deep copyin : \n{f}\n{m}")
    #copy.copy 2d array
    print(f"Copy copyin : \n{n}\n{i}")
    n = [[1,2,3], [4,5,6]]
    j[0][0] = [7,8,9]
    print(f"Deep copyin : \n{n}\n{j}")

