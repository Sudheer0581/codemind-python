n=int(input())
arr=list(map(int,input().split()))
st=set(arr)
s=0
c=0
for i in st:
    if(arr.count(i)==i):
        s=s+i
        c+=1
if(s==0):
    print("-1")
else:
    print("{:.2f}".format(s/c))