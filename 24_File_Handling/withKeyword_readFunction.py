''' By Using The With Keyword we are perfroming the file handling it work like normal 
file handling operation but only one thing is in that way we do not need to close the file

Syntax-  with open("Address/File Path",Mode) as File_object:
         operations
'''

with open("data.txt","r") as file_object:
    data=file_object.read()
    print(data)