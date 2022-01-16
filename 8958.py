n=int(input())

for i in range(n):

    result = 0
    total = []
    num=str(input())

    if num[0] == "O":
        result += 1
        total.append(result)
    else:
        total.append(result)

    for i in range(1,len(num)):
        if num[i-1]=="O" and num[i]=="O":
            result=total[i-1]+1
            total.append(result)
        elif num[i-1=="X"] and num[i]=="O":
            result=1
            total.append(result)
        else:
            result=0
            total.append(result)
    print(sum(total))
