n=int(input())
a=list(map(int,input().split()))
x=0
c=0
for j in range(max(a),0,-1):
    c=0
    for i in a:
        if i%j==0:
            c+=1
    if c==n:
        print(j)
        x=1
        break
if x==0:
    print("1")