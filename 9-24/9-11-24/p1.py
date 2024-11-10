# to find the lenght of the list

def printLen(list):
    for i in range(0,len(list)):
        print(list[i],end=" ")
    print()

num=[1,2,3,4,5,6,7,8,9]
sqr=[1,4,9,16,25]

printLen(num)
printLen(sqr)