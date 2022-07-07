def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input())
s=0
for i in str(n):
    s=s+fact(int(i))
if(s==n):
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")