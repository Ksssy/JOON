text = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
num=str(input())
num_cnt=[]

for i in text:
    num_cnt.append(num.count(i))
    num_replace = num.replace(f"{i}","")
    num=num_replace
    print(num)
print(num_cnt)
print(sum(num_cnt)+len(num))




s=input()
print(len(s)-sum(map(s.count,['c=','c-','dz=','d-','lj','nj','s=','z='])))