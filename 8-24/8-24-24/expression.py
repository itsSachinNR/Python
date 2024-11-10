# for string and numeric values use "*"
a,b=3,5
t="@"
print(a*t*b)

# for string and string values use "+"
c,d="1",4
t="@"
print((c+t)*d)

# numeric values can operates with all arithmetic operators
a,b=3,5
c=8
print(a+b*c)

# arithmetic expression with integers and float will result float
a,b=3,5.0
print(a+b)

# result of dividing operators with two integers will be float 
a,b=1,2
print(a/b)


# integer divison or floor(//) with float and int  will give int displayed as float(means if it is float it is 
# rounded off to nearest small intger)
a,b=1.5,2
c=a//b
print(c,a/b)

a,b=5,2
c=a//b
print(c,a/b)

a,b=-5,2
c=a//b
print(c,a/b)

a,b=5,-2
c=a//b
print(c,a/b)


# reminder is negative when denominator is negative

a,b=5,-2
print(a%b)

a,b=5,2
print(a%b)

a,b=-5,2
print(a%b)