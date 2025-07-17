x=[]
for i in range(1,(10**7)+1,2):
    x.append(i)
t=int(input("Enter Number of Testcase:"))  
for i in range(t):
    a=int(input())
    if a%2==0:
        print(x[:a-1])
    else:
        print(x[:a])
