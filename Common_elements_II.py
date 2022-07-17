n,m=map(int,input().split())
arr1=list(map(int,input().strip().split()))
arr2=list(map(int,input().strip().split()))
for i in arr1:
    if i not  in arr2:
        print(i,end=' ')
for i in arr2:
    if i not  in arr1:
        print(i,end=' ')
