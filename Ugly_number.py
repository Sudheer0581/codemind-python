n=int(input())
for i in range(n):
    while n%2==0:
        n=n//2
        
    if n==1:
        print("Ugly Number")
        break
    while n%3==0:
        n=n//3
    if n==1:
        print("Ugly Number")
        break
    while n%5==0:
        n=n//5
    if n==1:
        print("Ugly Number")
        break
else:
    print("Not Ugly Number")