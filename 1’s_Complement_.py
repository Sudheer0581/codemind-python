n=int(input())
l=[]
arr=[]
while(n!=0):
    r=n%2
    l.append(r)
    n=n//2
k=l[::-1]
for i in range(len(k)):
    if k[i]==1:
        arr.append(0)
    elif(k[i]==0):
        arr.append(1)
re=arr[::-1] # 1 0 1 0
s=0
for i in range(len(re)):
    s=s+(re[i]*2**i)
print(s)