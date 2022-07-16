n=int(input())
for i in range(n):
    m=int(input())
    arr=list(map(int,input().strip().split()))
    l=[]
    if m%2==0:
        for i in range(m//2):
            l.append(arr[m-i-1])
            l.append(arr[i])
    #print(*l)
    else:
        for i in range(m//2):
            l.append(arr[m-i-1])
            l.append(arr[i])
        l.append(arr[m//2])
    print(*l)
        