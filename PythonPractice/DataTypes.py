matrix = [[1,2,3],
          [2,3,4],
          [5,6,7]]
#2D list
#1D list
list1 = [1,2,3,4]
print(list1[:2])
list1.remove(1)
list1.append(5)
list1.insert(0,2)
list1.pop()
print(list1)

#can't modify
tupleExample = (1,2,3)
print(type(tupleExample))

#unpacking
x,y,z = tupleExample
print(x)

#dictonary
customer = {
    "name" : "Divya Y",
    "age" : 25,
    "height" : 75,
    "weight" : 80,
    "is_married" : False
}
print(customer["name"])
customer["qualifications"] = [
    {
        "name": "CSE",
        "age": 25,
    }
]
print(customer.get("name"))
print(customer.get("qualifications"))
print(customer.get("is_married"))