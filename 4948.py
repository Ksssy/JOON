def prime(number):
    if number==1:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


import sys
input = sys.stdin.readline

while True:
    result = 0
    n=int(input())
    if n == 0 :
        break
    for i in range(n,2*n+1):
        if prime(i):
            result += 1
    print(result)

