def prime(number):
    if number==1:
        return False
    else:
        for i in range(2, int(number**0.5)+1):
            if number%i == 0:
                return False
        return True

import sys
input = sys.stdin.readline
m,n = map(int,input().split())
for i in range(m,n+1):
    if prime(i):
        print(i)
