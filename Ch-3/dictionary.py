#creating a dictionary
# phone = {
#     "john" :8970483,
#     "ria" :5866903,
#     "joy" :6574382
# }
# print(phone)
 
#cheking type og dictionary
# print(type(phone))

#cheking the len of dictionary
# print(len(phone))
 
# #accesing the value of dictionary
# print(phone["john"])
# print(phone.get("john"))
# print(phone.keys())

# update value  in dict
# phone["john"]=345678
# print(phone)

# add value in dict
# phone["kia"]=2323646
# print(phone)

# more_phone={
#     "kia":1237
# }
# phone.update(more_phone)
# print(phone)

#remove the element in dict
# phone.pop("john")
# print(phone)

# phone.popitem()#this will  remove the  last added item
# print(phone)

# phone.clear() #this will empty
# print(phone)

# printing value of dict
# for x,y in phone.items():
#     print(x,y)

# nested dict
phone={
    "Area1": {
    "x":0,
    "y":1,
    "z":2
    },

    "Area2":{
    "a":3,
    "b":4,
    "c":5
    }
}
print(phone["Area1"]["y"])
print(phone["Area2"]["c"])


