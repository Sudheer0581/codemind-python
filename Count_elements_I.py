a,b=map(int,input().split())
arr1=list(map(int,input().strip().split()))
arr2=list(map(int,input().strip().split()))
l=[]
c=0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if(arr1[i]==arr2[j] and arr1[i] not in l):
            l.append(arr1[i])
            c+=1
print(c)