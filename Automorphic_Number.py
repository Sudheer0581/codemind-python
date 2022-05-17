n=int(input())
c=0
rev=0
t=0
temp=n
m=n*n
while(n):
    c+=1
    n//=10
for i in range(1,c+1):
    r=m%10
    rev=rev*10+r
    m//=10
while(rev):
    t=t*10+(rev%10)
    rev//=10
if(t==temp):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')