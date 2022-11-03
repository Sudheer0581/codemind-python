a,b=map(int,input().split())
l=list(map(int,input().split()))
z=list(map(int,input().split()))
k=[]
for i in z:
    if i in l and i not in k:
        k.append(i)
if(len(k)==len(z)):
    print("Yes")
else:
    print("No")
    