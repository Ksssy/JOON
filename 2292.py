n = int(input())
a = 1
b = 6
cnt = 1
if n == 1:
    print(cnt)
else:
    while True:
        a = a + b
        cnt += 1
        if n <= a:
            print(cnt)
            break
        b += 6


