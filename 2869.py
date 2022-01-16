import math

up,down,total = map(int,input().split())
day = math.ceil((total-up)/(up-down)) + 1
print(day)