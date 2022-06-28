r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))[:c]
    l.append(arr)
for i in range(c): # 0,1 
    max=l[0][i]
    for j in range(r):#0 1 2
        if(l[j][i]>max):
            max=l[j][i]
    print(max)