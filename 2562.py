a=0
b=0
for i in range(1,10):
    num=int(input())
    if a<=num:
        a=num
        b=i
    else:
        a=a
        b=b

print(a)
print(b)