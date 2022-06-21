n=int(input())
arr=list(map(int,input().strip().split())) # 3 2 3
q=set(arr) # 3 2
for i in q: # 3 2
    if(arr.count(i)>n//2): # 3--->2
        print(i)
        break
