n=int(input())
p=1
for i in range(n):
    m=int(input())
    for j in range(m,0,-1):
        p=p*j
    print(p)
    p=1