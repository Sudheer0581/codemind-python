n = list(map(str,input().split()))
for i in range(0,len(n)):
    for j in range(0,len(n)):
        if i!=j and len(n[i])<len(n[j]):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(*n)