n=int(input())
arr=list(map(int,input().split()))[:n]
l=[]
for i in range(len(arr)//2):
    l.append(arr[i])
    l.append(arr[n-i-1])
if(n%2!=0):
    l.append(arr[len(l)//2])
    l.append(0)
print(*l)