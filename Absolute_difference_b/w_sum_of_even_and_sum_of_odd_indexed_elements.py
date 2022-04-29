n=int(input())
s1=0
s2=0
a=list(map(int,input().strip().split()))[:n]
for i in range(n):
    if(i%2==0):
        s1=s1+a[i]
    if(i%2!=0):
        s2=s2+a[i]
print(abs(s1-s2))