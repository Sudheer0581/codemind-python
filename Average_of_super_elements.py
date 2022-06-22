n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
a=0
s=1
f=0
for i in arr:
    if i==arr.count(i) and i not in l:
        l.append(i)
        a=a+i
        f=1
if(f==1):
    s=a/len(l)
    print("{:.2f}".format(s))
else:
    print("-1")
    
