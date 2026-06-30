#copy() is in built list method used to create a shallow copy of a list
#it returns a new list contaning the same element as the orignall list
#copy data from source elemnt to destination element
"""
a=[1,2,3,4,5]
b=a
print(a)
print(b)
"""
a=[1,2,3,4,5,6]
b=a
b[0]=200
print(a)
print(b)