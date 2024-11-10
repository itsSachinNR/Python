dic={
    "name":"sachin",
    "age":19,
    "cgpa":8.45,
    "marks":{
        "cse":90,
        "ece":87,
        "mat":100
    }
}

# dic methods
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get("cgpa"))
print(dic.get("c")) #it dont give error when you type wrong key ,
# print(dic["cpa"]) #it give an error when you type wrong key
print(dic["cgpa"])

print(dic.update({"name" : "sunil"}))
print(dic.update({"name" : "sunil","place":"dvg"}))  #we can add or updated the alredy present key values
print(dic)


print(list(dic.keys()))
print(list(dic.values()))
print(list(dic.items()))
print(list(dic.keys()))