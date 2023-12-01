# 1]word wise reverse
def fn1(s):
    d=s.split(" ")
    print(d)
    for i in d:
        print(i[::-1],end=' ')
n=input('Enter the string:')
fn1(n)

# 2]two charachters interchange
print()
def fun1(s):
    d=s.split(" ")
    print(d)
    b= len(d)
    for i in d:
        for j in range(0,len(i),2):
            print(i[j:j +2][::-1],end='')
        print(end=' ')
n=(input("Enter the string:"))
fun1(n)
