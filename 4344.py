Tast_Case=int(input())
for i in range(Tast_Case):
    over_score=[]
    n=list(map(int,input().split()))
    avg=(sum(n)-n[0])/n[0]
    for j in range(1,len(n)):
        if n[j]>avg:
            over_score.append(n[j])
        else:
            continue
    print('%.3f'%((len(over_score)/n[0])*100)+"%")