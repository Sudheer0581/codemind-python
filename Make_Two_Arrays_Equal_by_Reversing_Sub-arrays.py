ts=int(input())
t=list(map(int,input().split()))
asi=int(input())
a=list(map(int,input().split()))
c=0
for i in t:
    if i in a:
        c+=1
if c==ts:
    print("True")
else:
    print("False")
