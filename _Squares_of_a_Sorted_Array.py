n=int(input())
arr=list(map(int,input().strip().split()))
s=[]
for i in range(len(arr)):
    s.append(arr[i]*arr[i])
s.sort()
print(*s)
    