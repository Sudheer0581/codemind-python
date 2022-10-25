t=int(input())
n=t*2
if(t>=3 and t<=100):
    for i in range(n//2):
        for j in range(i+1):
            print("*",end='')
        print()
    for i in range(n//2-1,0,-1):
        for j in range(i):
            print("*",end='')
        print()
else:
    print("The pattern is not possible")