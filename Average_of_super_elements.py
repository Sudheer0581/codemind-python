n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
s=0
k=0
l=[]
for i in range(n-1):
    for j in range(n):
        if(arr[i]==arr[j] and arr[i] not in l):
            c+=1
    if(c==arr[i]):
        l.append(arr[i])
    c=0
if(len(l)==0):
    print("-1")
else:
    for i in l:
        s+=i
    avg=s/len(l)
    print("{:.2f}".format(avg))