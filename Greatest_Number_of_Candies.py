n=int(input())
arr=list(map(int,input().strip().split()))
m=int(input())
x=max(arr)
for i in arr:
    if i+m>=x:
        print("True",end=' ')
    else:
        print("False",end=' ')
    