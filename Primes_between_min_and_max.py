n=int(input())
l=list(map(int,input().strip().split()))
maxi=l.index(max(l))
mini=l.index(min(l))
if(maxi<mini):
    mini,maxi=maxi,mini
c=0
for i in range(mini,maxi+1):
    if(l[i]<=1):
        continue
    else:
        for j in range(2,l[i]):
            if(l[i]%j==0):
                break
        else:
            c+=1
print(c)