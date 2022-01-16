num=[]
for i in range(10):
    n=int(input())
    num.append(n)

trash=[]
for j in num:
    num_x=int(j)%42
    trash.append(int(num_x))
print(len(set(trash)))