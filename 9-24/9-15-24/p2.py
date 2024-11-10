li=[1,2,'sachin',4,'sunil',6]

def lis(n):
    if(n==len(li)):
        return
    print(li[n])
    lis(n+1)
    
lis(0)