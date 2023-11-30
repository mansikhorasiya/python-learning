def udf_type(*args):
        print('tuple=',args)
        if type(args[0 ][0])==list:
            a=[item for b in args[0]for item in b]
            square=list(map(lambda x:x*x,a))
            odd=list(filter(lambda x:(x %2 !=0),a))
            print("square=",square)
            print("odd=",odd)
        else:
            if len(args) == 1:
                print("List=", args[0])

            elif len(args) == 2:
                args[0].extend(args[1])
                print("Maximum Element=", max(args[0]))
                print("Minimum Element=", min(args[0]))
            elif len(args) == 3:
                args[0].extend(args[1])
                args[0].extend(args[2])
                print("Sum=", sum(args[0]))

no_list = int(input('Enter number of list:'))
if no_list == 1:
        a = int(input("Enter Number Of elements:"))
        list1 = []
        for i in range(a):
            list1.append(int(input("Enter elements:")))
        # print(list1)
        udf_type(list1)

elif no_list == 2:
        list1 = []
        list2 = []
        a1= int(input("Enter Number of elements:"))
        for i in range(a1):
            list1.append(int(input("Enter elements:")))
        print(list1)
        a2=int(input("Enter Number of elements:"))
        for i in range(a2):
            list2.append(int(input("Enter elements:")))
        print(list2)
        udf_type(list1,list2)
elif no_list==3:
        list1 = []
        list2 = []
        list3 = []
        a1=int(input("Enter number of elements:"))
        for i in range(a1):
            list1.append(int(input("Enter elements:")))
        print(list1)
        a2= int(input("Enter Number of elements:"))
        for i in range(a2):
            list2.append(int(input("Enter elements:")))
        print(list2)
        a3=int(input("Enter Number of elements:"))
        for i in range(a3):
            list3.append(int(input("Enter elements:")))
        print(list3)
        udf_type(list1, list2,list3)
else:
        main_list=[]
        for i in range(no_list):
            b = int(input("Enter Number of elements for List{}=".format(i)))
            ls=[]
            for j in range(b):
                ls.append(int(input("Enter element for list{}=".format(i))))
        main_list.append(ls)
        print('main_list',main_list)
        udf_type(main_list)












