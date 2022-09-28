n=int(input())
arr=list(map(int,input().strip().split()))
for i in range(0,(n//2)+1,2):
    for j in range(arr[i]):
        print(arr[i+1],end=' ')  # 1 2 3 4