x=int(input())
n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    if(a<x or b<x):
        print("UPLOAD ANOTHER")
    else:
        if(a==b):
            print("ACCEPTED")
        else:
            print("CROP IT")