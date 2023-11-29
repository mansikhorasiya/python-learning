studentInfo = open("studentInfo.txt", "w+")

studentMarks = open("studentMarks.txt", "w+")

aGrade = open("Agrade.txt", "w+")

bGrade = open("Bgrade.txt", "w+")

cGrade = open("Cgrade.txt", "w+")


def fn1(nostu):
    for i in range(nostu):
        rollno = input("Enter Roll No=")
        name = input("Enter Name=")
        studentInfo.write(rollno + "-" + name + "\n")
        studentMarks.write(rollno)
        for j in range(3):
            marks = input("Enter marks of student:")
            studentMarks.write("-" + marks)

        studentMarks.write("\n")


def fn2():
    studentInfo.seek(0)
    studentMarks.seek(0)
    ls1 = studentInfo.readlines()
    ls2 = studentMarks.readlines()
    print(ls1, ls2)
    return ls1, ls2


def fn3(ls1, ls2):
    # ['1-a\n', '2-b\n', '3-c\n']
    # ['1-99-99-99\n', '2-88-88-88\n', '3-77-77-77\n']
    ls3 = []
    ls4 = []
    for i in ls1:
        dummy = i.replace("\n", "")
        templs = dummy.split("-")
        ls3.append(templs)

    for j in ls2:
        dummy = j.replace("\n", "")
        templs = dummy.split("-")
        avg = (int(templs[1]) + int(templs[2]) + int(templs[3])) // 3
        ls4.append([templs[0], str(avg)])
    print("ls3>>>>>>>>>>>>>>>>>>>>>>>", ls3)
    print("ls4>>>>>>>>>>>>>>>>>>>>>>>", ls4)
    return ls3, ls4


def fn4(ls3, ls4):
    # [['1', 'a'], ['2', 'b'], ['3', 'c']]
    # [['1', '99'], ['2', '88'], ['3', '77']]

    ls5 = []
    averageSet = {0}
    for i in ls3:
        for j in ls4:
            if i[0] == j[0]:
                dummy = i[0] + "-" + i[1] + "-" + j[1]
                averageSet.add(int(j[1]))
                ls5.append(dummy.split("-"))

    sortedList = list(averageSet)
    sortedList.sort(reverse=True)
    print("averageSet>>>>>>>>>", averageSet)
    # {0, 88, 99, 77}
    print("sortedList>>>>>>>>>", sortedList)
    # [99, 88, 77, 0]
    print("ls5>>>>>>>>>>>>>>>", ls5)
    # [['1', 'a', '99'], ['2', 'b', '88'], ['3', 'c', '77']]

    for i in sortedList:
        for j in ls5:
            if int(j[2]) == i and 80 < int(j[2]) <= 100:

                aGrade.write(j[0] + "-" + j[1] + "-" + j[2] + "\n")

            elif int(j[2]) == i and 60 < int(j[2]) <= 80:

                bGrade.write(j[0] + "-" + j[1] + "-" + j[2] + "\n")

            elif int(j[2]) == i and 40 < int(j[2]) <= 60:
                cGrade.write(j[0] + "-" + j[1] + "-" + j[2] + "\n")


nostu = int(input("Enter No. Of students:"))

fn1(nostu)

ls1, ls2 = fn2()

ls3, ls4 = fn3(ls1, ls2)

fn4(ls3, ls4)

studentInfo.close()

studentMarks.close()