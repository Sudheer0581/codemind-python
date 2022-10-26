n=int(input())  #25173917
l=list(map(int,input().split()))
s=0
c=0
for i in range(0,n-1,2): # 0 2 4 6 8 
    if(l[i]>l[i+1]):
        s+=1
    else:
        c+=1
if(s==n//2 or c==n//2):
    print("yes")
else:
    print("no")