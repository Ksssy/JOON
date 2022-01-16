def result(a):
    b,c,d=str(a)[0],str(a)[1],str(a)[2]
    return b,c,d

n=int(input())
result_1=[]
if n<100:
    print(n)
elif n>=100:
    for i in range(100, n + 1):
        b, c, d = result(i)
        if int(b) - int(c) == int(c) - int(d):
            result_1.append(i)
    print(len(result_1)+99)
