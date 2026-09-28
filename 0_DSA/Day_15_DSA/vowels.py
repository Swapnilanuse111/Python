s=input("Enter The String")
count=0
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count=count+1
print("in this String There are ",count,"Vowels are present")