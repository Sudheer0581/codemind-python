n=int(input())
p=str(n)
s=0
j=0
for i in range(1,len(p)+1):
   s=s+int(p[j])**i 
   j+=1 
if(n==s):
    print("True")
else:
    print("False")