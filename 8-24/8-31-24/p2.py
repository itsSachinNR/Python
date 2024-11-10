lis=[]
lis.append(input("enter the number 1: "))
lis.append(input("enter the number 2: "))
lis.append(input("enter the number 3: "))
lis.append(input("enter the number 4: "))
lis.append(input("enter the number 5: "))
lis.append(input("enter the number 6: "))

if(lis[0]==lis[5]):
    if(lis[1]==lis[4]):
        if(lis[2]==lis[3]):
            print("palidrome")
        else:
            print("1")
    else:
        print("2")
else:
    print("3")