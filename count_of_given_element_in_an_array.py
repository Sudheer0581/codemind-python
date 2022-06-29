n=int(input())
arr=list(map(int,input().strip().split()))
a=int(input())
c=0
for i in arr:
    if(i==a):
        c+=1
print(c)
