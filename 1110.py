k=int(input())
n=k
i=[]
while True:
    if n >= 10:
        a = n % 10
        b = (n - a) / 10
        c = a + b
        d = c % 10
    else:
        a = n
        b = 0
        c = a + b
        d = c % 10

    n = 10 * a + d
    i.append(n)
    if n==k:
        break
print(len(i))