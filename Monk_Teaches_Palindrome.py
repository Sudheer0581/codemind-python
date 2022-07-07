n=int(input())
for i in range(n):
    a=input() 
    q=a[::-1] 
    if(a==q and len(a)%2==0):
        print("YES EVEN")
    elif(a==q and len(a)%2!=0):
        print("YES ODD")
    else:
        print("NO")