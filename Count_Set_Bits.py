for i in range(int(input())):
    x=int(input())
    l=[]
    while(x!=0):
        r=x%2
        l.append(r)
        x=x//2
    print(l.count(1))