num = int(input("Say: "))
string = "hello to the world {0:2.3f} times"
new_string = string.format(num)
print(new_string)