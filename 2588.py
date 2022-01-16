a=int(input())
b=int(input())

c=int(b%10)
d=int((b%100-c)/10)
e=int((b-(d*10+c))/100)

print(a*c)
print(a*d)
print(a*e)
print(a*b)