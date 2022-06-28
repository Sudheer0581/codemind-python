n=int(input())
arr=list(map(int,input().strip().split()))
c=0
for i in arr:
    if i==0:
        c+=1
    if i<0:
        i=i*-1
    while(i):
        i=i//10
        c+=1
    print(c,end=' ')
    c=0

        