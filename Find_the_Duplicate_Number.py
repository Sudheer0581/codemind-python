n=input()
arr=list(map(int,input().strip().split()))
for i in arr:
    if arr.count(i)>=2:
        print(i)
        break