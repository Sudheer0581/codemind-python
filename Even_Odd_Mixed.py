n=int(input())
e=0
o=0
for i in str(n):
    if(int(i)%2==0):
        e+=1
    else:
        o+=1
if(e==len(str(n))):
    print("Even")
elif(o==len(str(n))):
    print("Odd")
else:
    print("Mixed")