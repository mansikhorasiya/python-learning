input_tuple = (1,2,3,4,5,6)

list = []

#adding revers values in list
for x in reversed(input_tuple):
    list.append(x)

output_tuple=tuple(list) #type cast  into tuple
print(output_tuple)
