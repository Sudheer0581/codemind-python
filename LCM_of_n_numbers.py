n=int(input())
a=list(map(int,input().split()))
i=1
c=0
while(i>0):
    c=0
    for j in a:
        if i%j==0:
            c+=1
    if c==n:
        print(i)
        break
    else:
        i+=1