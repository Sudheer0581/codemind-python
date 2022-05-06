m,n=map(int,input().split())
for i in range(1,n+1):
    c=m*i
    if(c%n==0):
        print(c)
        break