n=int(input())
a=list(map(int,input().strip().split()))
b=set(a)
s=0
for i in b:
    if a.count(i)==1:
        print(i,end=" ")
        s=1
if s==0:
    print("-1")

        
