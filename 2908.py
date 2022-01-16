a,b=input().split()

a_num=a[::-1]
b_num=b[::-1]

if a_num > b_num:
    print(a_num)
else:
    print(b_num)