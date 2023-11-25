# pass by value
def addOne(x):
    x = x + 1
    print("Inside the functrion:",x)

x=5
addOne(x)
print("out the function:",x)

# pass by reference
def modifylist(lst):
    lst.append(4)
    print("Inner function:",lst)
lst=[1 , 2 , 3]
modifylist(lst)
print("outside  function:",lst)
