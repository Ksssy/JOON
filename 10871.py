N,X=[int(i) for i in input().split()]

A=list(map(int,input().split()))
for i in A:
    if i<X:
        print(i,end=' ')