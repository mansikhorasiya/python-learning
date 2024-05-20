# def maximum(a,b):
#     if a >= b :
#         return a
#     else:
#         return b

# a=2
# b=4
# print(maximum(a,b))

# using lambda function
a=-1;b=-4
maximum = lambda a,b: a if a > b else b
print(f'{maximum(a,b)} is  a maximum number')