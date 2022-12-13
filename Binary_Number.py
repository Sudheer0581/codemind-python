def binary(x):
    l=''
    while(x>0):
        r=x%2
        l+=str(r)
        x=x//2
    while(len(l)<n):
        l+='0'
    l=l[::-1]
    return l
n=int(input())
l=[]
t=0
for i in range(2**n):
    print(binary(i))