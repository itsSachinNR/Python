with open("practice.txt","w") as f:
    f.write("Hi everyone \nwe are learning File I/O\nusing java\nI like programing in java")


with open("practice.txt","r") as f:
    data=f.read()
    
new_data=data.replace("java","python")
print(new_data)
print(data)

with open("practice.txt","w") as f:
    f.write(new_data)

with open("practice.txt","r") as f:
    data=f.read()
    print(data)