m = int(input())
n = int(input())
result = []
for i in range(m,n+1):
    for j in range(2,i+1):
        if i == j:
            result.append(i)
        if i%j == 0:
            break

if len(result) == 0:
    print("-1")
else:
    print(sum(result))
    print(result[0])