n=int(input())
for i in range(n):
    m=int(input())
    temp=m
    rev=0
    l=''
    while(temp>0):
        r=temp%2
        l+=str(r)
        temp//=2
    print(l[::-1])
        
        