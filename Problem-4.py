x=list(map(int,input().split(",")))
res={}
for i in range(1,10):
    c=0
    for j in x:
        if j%i==0:
            c+=1
    res[i]=c
print(res)
        
