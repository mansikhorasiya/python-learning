#creating a set
# name = {"sia","mia","tia"}
# print(name)

# print(type(name))

# print(len(name))

#accesing item of set
# for i in name:
#     print(i)

#add to set
# name.add("ria")
# print(name)

#remove to set
# name.remove("tia")
# name.discard("ria") #this function not through the error  if value is not present  in set
# print(name)


#add another sequence in a set
# name_list=["ria","kia"]
# name.update(name_list)
# print(name)

#join two set
s1 ={'a','b','c'}
s2={'e','f','a'}

print(s1,s2)
# s3=s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

#keep only duplicates value
# s1.intersection(s2)
# print(s1)

#keep  all value except duplicat value
s1.symmetric_difference_update(s2)
print(s1)