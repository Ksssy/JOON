def result(n):
    n=n+sum(map(int,str(n)))
    return n
a=[]
for i in range(1,10001):
    a.append(result(i))

for i in range(1,10001):
    if (i not in a):
        print(i)