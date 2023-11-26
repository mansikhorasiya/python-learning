# reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
tuple1=tuple1[::-1]
print(tuple1)

# access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])

# create a tuple  with   single  item 50
tuple1=(50,)
print(tuple1)

# unpack the  tuple into 4 variable
tuple1 = (10, 20, 30, 40)

# unpack tuple into 4 variables
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)
 

#10] Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))

