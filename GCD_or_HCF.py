a,b=map(int,input().strip().split())
if(a<b):
    for i in range(1,a+1):
        if(a%i==0) and (b%i==0):
            f=i
    print(f)