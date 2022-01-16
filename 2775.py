test_case=int(input())
cnt=0
while True:
    cnt += 1
    k=int(input())
    n=int(input())
    k_0 = []
    for i in range(1,n+1):
        k_0.append(i)
    for i in range(1,k+1): # 1층 부터 k 층까지
        k_1=[1]
        for j in range(1,n): # 2호실부터 n호실까지
            k_1.append(sum(k_0[0:j+1]))
        k_0=k_1
    print(k_0[n-1])

    if cnt == test_case:
        break