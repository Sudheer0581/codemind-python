t=int(input())
for i in range(t):
    a=input()
    x=a[0]
    y=a[0]
    for i in range(1,len(a)):
        if x!=a[i]:
            x=a[i]
            y+=a[i]
    print(len(a)-len(y))
        