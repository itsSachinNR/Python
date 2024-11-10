# find the factorial a number n

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)
    

fact(5)
fact(8)
fact(14)