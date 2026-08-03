#Constuructor is inbuild or predfined method in pyhthon which is used to initilize the object member as well
#constucor is consider as self invoking method as it is automaticlly executed whenever obect is created or initilized 
class Bank:
    name="SBI"
    def __init__(self):
        pass
S1=Bank()
print("Before modifing the class member ")
print(S1.name)
S1.name="ICIC"
print("After Modifing the class memeber")
print(S1.name)