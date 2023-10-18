n=int(input("no of elements in series ="))
fab=[]
x,y=0,1
for i in range(n):
    fab.append(x)
    x,y=y,x+y
print(fab)
