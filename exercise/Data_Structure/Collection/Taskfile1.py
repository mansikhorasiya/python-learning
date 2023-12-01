ls = [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6, ['d', 'e', 'f'], 7, 'g', 8, 'h', [9, 10, 'i', 'j'],11,'aansh']

for i in ls:
        if type(i) == list:
                for j in i:
                    if type(j) == str:
                        print(' ',j)

                    else:
                          print(j)
        elif type(i) ==str:
              print(' ',i)
        else:
              print(i)