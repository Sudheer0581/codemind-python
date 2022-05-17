n=int(input())
s=0
while(True):
    s=0
    while(n):
        r=n%10
        s=s+r
        n//=10
    if(s<=9):
        print(s)
        break
    else:
        n=s
        