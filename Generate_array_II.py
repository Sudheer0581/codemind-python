n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a),2):
    for j in range(1,a[i+1]+1):
        print(a[i],end=" ")