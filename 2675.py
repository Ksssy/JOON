test=int(input())

for i in range(test):
    r,s=input().split()
    p=""
    for j in range(len(s)):
        p=p+int(r)*s[j]
    print(p)

