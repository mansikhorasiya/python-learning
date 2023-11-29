abc = open('Demo.txt','w+')
def fn1():
    n= int(input("Enter the num of line:"))
    for i in range(n):
        a = input("Enter data:")
        abc.write(a+"\n")
        print(a)
def read_data():
    abc.seek(0)
    data1 = abc.read()
    print(data1)
# count line
    line = data1.count("\n")
    print("total Line:",line)
# words
    word = data1.split()
    print(word)
    print("number of words:",len(word))
# with space
    space = data1.count(' ')
    word_with_space = (len(data1))
    print("word with space ",word_with_space)
# without space
    word_without_space = (word_with_space) - (space) - (line)
    print("word without space:",word_without_space)
fn1()
read_data()
