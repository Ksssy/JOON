n = int(input())
num = []
for i in range(2,n+1):
    for j in range(2,i+1):
        if i == j:
            num.append(i)
        if i % j == 0 :
            break

n_num = [i for i in num if i<=n//2 or n == i]

while True:
    for i in range(len(n_num)):
        if n%n_num[i] == 0:
            print(n_num[i])
            n = n//n_num[i]
            break

    if n == 1:
        break
