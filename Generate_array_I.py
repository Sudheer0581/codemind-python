n=int(input())
arr=list(map(int,input().strip().split()))
for i in range(0,len(arr),2):
    for j in range(1,arr[i+1]+1):
        print(arr[i],end=' ')