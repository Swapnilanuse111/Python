'''Operations On File Handling

#read() function
---->A read() function is a type of function which is used to read the context from entire file

----->By Using read function We Can Fetch Or Asses The The All Entire text Context in the filee
'''

file_object = open('data1.txt','r')
data = file_object.read()
print(data)
file_object.close()