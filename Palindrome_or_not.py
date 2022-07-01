def palin(n):
    q=n[::-1]
    if(n==q):
        return True
    else:
        return False
n=input()
s=n.split()
for i in s:
    if palin(i.lower()):
        print("True")
        break
else:
    print("False")