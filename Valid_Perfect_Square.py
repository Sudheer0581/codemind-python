n=int(input())
f=0
for i in range(n):
    m=int(input())
    for j in range(1,m//2+1):
        if(m==j*j):
            f=1
            break
    if(f==1):
        print("True")
    else:
        print("False")
    f=0