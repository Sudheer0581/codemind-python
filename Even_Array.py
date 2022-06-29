n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
s=arr
for i in arr:
    if i%2==0:
        l.append(i)
if len(l)==len(s):
    print("True")
else:
    print("False")