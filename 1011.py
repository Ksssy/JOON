import sys

test_case = int(input())
test = 0
while True:
    test += 1
    x,y=map(int,sys.stdin.readline().split())
    distance = y - x
    k = distance ** 0.5
    k = int(k)
    if distance == k*k :
        cnt = 2*k-1
    elif distance > k*k and distance <= k * (k+1) :
        cnt = 2*k
    elif distance > k * (k+1) and distance <= k * (k+2) :
        cnt = 2*k+1
    print(cnt)

    if test == test_case :
        break