def binary(n):
    x=int(n)
    temp=x
    s=0
    t=0
    while(temp>0):
        r=temp%10
        s+=r*(2**t)
        temp//=10
        t+=1
    return s
n=int(input())
for i in range(n):
    arr=input()
    arr=arr[::-1]
    x=''
    z=''
    for i in arr:
        x+=str(i)
    l=[]
    for i in range(0,len(x),3):
        f=x[i:i+3]
        l.append(f)
    for i in l:
        i=i[::-1]
        z+=(str(binary(i)))
    print(z[::-1])
        
     
        
    