n=int(input())
total=[int(i) for i in input().split()]

max_score=max(total)

re_total=[]
for i in total:
    a=(i/max_score)*100
    re_total.append(a)

result=sum(re_total)/n

print(result)