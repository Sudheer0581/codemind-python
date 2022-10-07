n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    c=0
    for i in range(0,b+1):
        if (i*i)%b==a:
            print(i)
            c=1
            break
    if(c==0):
        print('-1')