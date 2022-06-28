n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
c=arr.count(0)
for i in range(c):
    arr.remove(0)
    l.append(0)
arr.extend(l)
print(*arr)