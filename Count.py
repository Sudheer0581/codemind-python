n=int(input())
arr=list(map(int,input().strip().split()))
c=0
o=0
for i in range(n):
    if arr[i]%2==0:
        c+=1
    else:
        o+=1
print(c,o,end=" ")