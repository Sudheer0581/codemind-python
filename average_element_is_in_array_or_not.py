n=int(input())
arr=list(map(int,input().strip().split()))
s=0
for i in arr:
    s=s+i
avg=s//n
for i in arr:
    if i==avg:
        print("True")
        break
else:
    print("False")