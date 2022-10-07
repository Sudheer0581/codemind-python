def res(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 4
    else:
        return res(x-1)+res(x-2)+res(x-3)
n=int(input())
print(res(n))