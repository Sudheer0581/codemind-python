n=int(input())
for i in range(n):
    m=int(input())
    l=[]
    k=0
    s=0
    while(m>0):
        r=m%10
        l.append(r)
        m=m//10
    for i in range(len(l)):
        s+=l[i]*(2**k)
        k+=1
    print(s)