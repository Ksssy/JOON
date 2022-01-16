a,b=map(int, input().split( ))

b-=45
if b<0:
    b+=60
    if a==0:
        a=23
    else:
        a-=1

print(a, b)