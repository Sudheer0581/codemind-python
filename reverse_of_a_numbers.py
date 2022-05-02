n=int(input())
rev=0
temp=n
while(temp):
    r=temp%10
    rev=rev*10+r
    temp=temp//10
print(rev)