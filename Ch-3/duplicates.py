l1=[1,2,3,4,4]
l2=[2,3,4,5,6,7]
l3=[5,6,7,8,4,5]

#type casting
s1=set(l1)
s2=set(l2)
s3=set(l3)

#join the intersection
s1s2=s1.intersection(s2)
final_set=s1s2.intersection(s3)

final_list=list(final_set)
print(final_list)