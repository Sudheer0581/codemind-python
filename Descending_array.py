n=int(input())
arr=list(map(int,input().strip().split()))
for i in range(1,n):
    if arr[i]>arr[i-1]:
        print("no")
        break
else:
    print("yes")