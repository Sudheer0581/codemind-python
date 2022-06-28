n=int(input())
for i in range(n):
    a=int(input())
    s=str(a)
    l=list(s)
    l.sort()
    c=1
    for i in range(len(l)-1):
        if(int(l[i+1])-int(l[i])==1):
            c+=1
    if(c==len(l)):
        print("YES")
    else:
        print("NO")