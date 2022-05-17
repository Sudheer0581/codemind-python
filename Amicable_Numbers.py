x=int(input())
y=int(input())
s1=0
s2=0
for i in range(1,x):
    if x%i==0:
        s1+=i
for j in range(1,y):
    if y%j==0:
        s2+=j
if(s1==y and s2==x):
    print("Amicable")
else:
    print("Not Amicable")