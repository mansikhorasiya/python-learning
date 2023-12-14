#
# n=int(input("Enter the number of element:"))
# ls=[]
# for i in range(n):
#     element=int(input('Enter elements{}:'.format(i+1)))
#     print(element)
#     ls.append(element)
# print('list:',ls)

# total_sum=sum(ls)
# print('total_sum',total_sum)

# half_total=total_sum//2
# print('half_total',half_total)

# ls.sort(reverse=True)
# ls1=[]
# ls2=[]


# if total_sum %2==0 and half_total>=max(ls):
#     for i in ls:
#         if sum(ls1)<=sum(ls2):
#             ls1.append(i)
#         else:
#             ls2.append(i)
# print('ls1',ls1)
# print('ls2',ls2)

# print('sum of ls1:',sum(ls1))
# print('sum of ls2:',sum(ls2))
# >>>>>>>>>list[7,4,14,3,8,6]
ls=[7,4,14,3,8,6]
ls1=[]
ls2=[]

print("list :", ls)

total_sum = sum(ls)
print("Total Sum : ",total_sum)

half_total=total_sum // 2
print("Half_total : ",half_total)

ls.sort(reverse=True)

if total_sum % 2 == 0 and half_total >= max(ls):
    for i in ls:
        if sum(ls1) < sum(ls2):
            ls1.append(i)
        else:
            ls2.append(i)

    print('ls1', ls1)
    print('ls2', ls2)

    print('sum of ls1', sum(ls1))
    print('sum of ls2', sum(ls2))

    if sum(ls1)==sum(ls2):

        print('ls1',ls1)
        print('ls2',ls2)

        print('sum of ls1:',sum(ls1))
        print('sum of ls2:',sum(ls2))

    else:
        for i in ls1:
            for j in ls2:

                ls1_sum = sum(ls1)
                ls2_sum = sum(ls2)

                temp1=ls1_sum-i+j
                temp2=ls2_sum-j+i

                if temp1==temp2:
                    ls1.remove(i)
                    ls1.append(j)
                    ls2.append(i)
                    ls2.remove(j)

        print("New ls1 :",ls1)
        print("New ls2 :",ls2)

        print("New ls1 SUM : " , sum(ls1))
        print("New ls2 SUM : " , sum(ls2))

else:
    print("Invalid List :")
