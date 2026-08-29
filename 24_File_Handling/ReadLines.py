'''
readlines() Function

-----> The readlines() function is used to read or fetch
all the lines present in a file.

-----> It returns all the lines from the file in the form of a list.
'''
file_object=open('abc.txt','r')
var=file_object.readlines()
print(var)