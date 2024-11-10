# create a student class that takes name and 3 subject marks as parameter in constructor,
# then create a method to print the avg 

class Student:
    def __init__(self, name, a, b, c):
        self.name=name
        self.a=a
        self.b=b
        self.c=c
        
    def average(self):
        avg=self.a+self.b+self.c
        print(self.name, "your average marks is :",avg/3)
        

s1=Student("sachin", 8,7,9)
s1.average()


s1.name="sunil"
s1.average()