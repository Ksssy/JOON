test_case = int(input())
test=0
while True:
    test += 1
    h, w, n = map(int, input().split())
    y = n % h
    x = n // h
    if y==0:
        print(h,'%02d'%x,sep='')
    else:
        print(y,'%02d'%(x+1),sep='')
    if test==test_case:
        break