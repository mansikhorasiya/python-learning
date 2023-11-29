abc = open('Demo1.txt','w+')
fo = open('Dummy.txt','w+')

def write_data():
    n= int(input("Enter the line: "))

    for i in range(n):
        a = input("Enter the data:")
        abc.writelines(a+'\n')

def read_data():
    abc.seek(0)
    num_line = abc.readlines()
    num_line.reverse()
    print(">>>>>>>",num_line)
    fo.writelines(num_line)

def replace():
    fo.seek(0)
    rev_data = fo.read()
    old_data =input("Enter old data:")
    new_data =input("Enter new data:")
    fo.seek(0)
    repl_data =rev_data.replace(old_data,new_data)
    print(">>>>>>>",repl_data)
    fo.write(repl_data)

write_data()
read_data()
replace()

