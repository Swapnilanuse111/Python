#1St approch
num=int(input("Enter the number"))
m_sum=str(num) # here we are convetring numbre which will in the form of integer to string 
print(len(m_sum))#and using the len function calculate the how manny digits are  the the varible

#Seceond Approch
num=int(input("Enter the number"))
count=0     #using the count varible we are 
while num!=0:
    count=count+1
    num=num//10
print(count)