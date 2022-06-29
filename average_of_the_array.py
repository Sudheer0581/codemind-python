n=int(input())
arr=list(map(int,input().strip().split()))
s=0
for i in arr:
    s=s+i
avg=s/n
print("{:.2f}".format(avg))