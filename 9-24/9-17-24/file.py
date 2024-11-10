# f=open("C:\Users\tee\Desktop\yout\python\9-17-24\sample.txt")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

f = open("C:\\Users\\tee\\Desktop\\yout\\python\\9-17-24\\sample.txt")
# data= f.read() #read everything in the file
data= f.read(7) # we can tell number of char to read
print(data)
print(type(data))
f.close()