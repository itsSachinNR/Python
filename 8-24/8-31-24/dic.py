# dictionary

# dic={
#     "name":"sachin",
#     "age":19,
#     "cgpa":8.45
# }

# print(dic)
# print(dic["age"])
# print(dic["name"])
# print(dic["cgpa"])

# dic["section"]="3cit02"
# print(dic)
# dic["age"]=18
# print(dic)



# nested dic

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

print(dic)
print(dic["age"])
print(dic["marks"])
print(dic["marks"]["cse"])
print(dic["marks"]["mat"])
print(dic["marks"]["ece"])

