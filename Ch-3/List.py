fruits = ["Apple","Banana","Cheryy"] #How to create a list

print(fruits) #print a list

# print(type(fruits)) #cheak the list type

# print(len(fruits)) #cheak lenght of list

# #cheaking if  an item is a present in the list
# if "Banana"in fruits:
#     print("banana is present in the list..")

# #cheaking if an item is a not presenyt in the list
# if "kiwi" not in fruits:
#     print("kiwi us not present in the list..")

# # Indexing 
# print(fruits[1]) #Banana
# print(fruits[-2]) #Banana

# print(fruits[0:2]) #["Apple","Banana"]
# print(fruits[-3:-1]) #["Apple","Banana"]

#adding  elements in list
# fruits.append("kiwi")
# print(fruits)

# fruits.insert(2,"kiwi")
# print(fruits)

# more_fruits=["papaya","kiwi"]
# fruits.extend(more_fruits)
# print(fruits)

#removing elemets from the list
# fruits.remove("Banana")
# print(fruits)
 
# fruits.pop()
# print(fruits)

# fruits.pop(1)
# print(fruits)

#chaning/update list
# fruits[1]="kiwi"
# print(fruits)

# fruits[1:3]=["papaya"]
# print(fruits)

# sort a list
#fruits.sort() #by deafult asending order
# fruits.sort(reverse=True)
# print(fruits)

# fruits.reverse()
# print(fruits)

#list comprehension
# new_fruits=[fruit for fruit in fruits if "a" in fruit]
# print(new_fruits)

#copy list
# new_fruits=fruits.copy()
# print(new_fruits)

# new_fruits=fruits + new_fruits
# print(new_fruits)

#nested list
fruits.insert(1,["kiwi","papaya"])
print(fruits)
print(fruits[1][0])