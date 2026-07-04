#it is a datatype which store all data in key value pair formate
list={
    "name":"swapnil",
    "age":22,
    "Address":"Pune"
}
print(list)

#opration in dictonary

#accsess the values using element
print("Using The Key Getting the element from the Dic")
print(list["name"])

#geting the value using get()

print("get function used to getting the value using the key")
print(list.get("Address"))
list["name"]="anuse"
print(list)


Student={
    "name":"Rahul",
    "age":27,
    "address":"Atpadi"
}
print(Student)
print("using the update method we can Easily Update the Keys And values on the  dic")
Student.update({
    "name":"swapnil",
    "age":22,
    "address":"pune"
})
print(Student)

#removing the element using pop opration

a={
    "name":"swap",
    "age":"12"
}
print(a)
print("Using the pop opration removing specfic element from the dic using the Key")
a.pop("age")
print(a)


#Remove Last Item using popitem()
student = {
    "name": "Swapnil",
    "age": 22,
    "address":"karagani"
}
student.popitem()
print(student)
print(len(student))
