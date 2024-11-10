# find the factorial of the first n numbers

n=int(input("enter n: "))

for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    print(fact)
