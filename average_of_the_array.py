n=int(input())
s=0
a=list(map(int,input().strip().split()))
for i in range(n):
    s=s+a[i]
c=s/n
print("%.2f"%c)