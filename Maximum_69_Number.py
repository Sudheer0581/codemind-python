def reverse(num):
    rev=0
    while(num):
       r=num%10
       rev=rev*10+r
       num//=10
    return rev
a=int(input())
r=reverse(a)
c=0
rev=0
while(r):
    rem=r%10
    if(c==0 and rem==6):
        rem=9
        c=1
    rev=rev*10+rem
    r//=10
print(rev)