n=int(input())
l=list(map(int,input().strip().split()))
s=0
for i in l:
    s=s+i
if(s%2==0):
    print("1")
else:
    print("0")