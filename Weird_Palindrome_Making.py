t=int(input())
for i in range(1,t+1):
    x=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in a:
        if i%2==1:
            c+=1
    print(c//2)