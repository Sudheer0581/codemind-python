a,b,c=map(int,input().split())
count=0
for i in range(a,b+1):
    if(i%c==0):
        count+=1
print(count)