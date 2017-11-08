#==========================function=======================================================================
def dictFun(y,p,q):
    t = {}
    j = 0
    for i in range(p,q+1):
        t[i] = y[j]
        j= j+1
    return t

def keysFun(y):
    t = []
    for i in y.keys():
        t.append(i)
    return set(t)

def convolution(u,v):
    e = keysFun(u)
    f = keysFun(v)
    y = {}
    sum = 0
    for i in range(min(e.intersection(f)),max(e.intersection(f))+1):
        sum = sum+(u[i]*v[i])
    return sum
#=========================input=====================================================================
a = list(map(int,input("Enter X function\n").split()))
m = int(input("Enter the position of zeroth index in function X\n"))

b = list(map(int,input("Enter H function\n").split()))
n = int(input("Enter the position of zeroth index in function H\n"))

p = 1-m
q = len(a)-m
r = 1-n
s = len(b)-n
u = dictFun(a,p,q)
    
for i in range(len(b)-n+1+len(a)-m):
    v= dictFun(b,-s+i,-r+i)
    print(convolution(u,v),end=" ")
