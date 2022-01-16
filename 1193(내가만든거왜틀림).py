"""
a 번째 대각선의 b 번째인가?
를 보면
5번째 대각선의 3번째
즉 y열은 b를 그대로 따라감
   x 열은 a-b+1이 됨
즉 분수는 b/(a-b+1)이라는 숫자가 나옴
"""

n=int(input())
num=1
up=2
if n==1:
    print("1/1")
else:
    while True:
        num = num + up
        if n<=num:
            a = up
            b = n-(num-up)
            print(f"{b}","/",f"{a-b+1}",sep='')
            break
        up += 1
