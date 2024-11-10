# find the sum of n numbers using recursion

def num(n):
    if(n==0):
        return 0
    return n + num(n-1)

print(num(5))