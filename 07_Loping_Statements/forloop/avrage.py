#for finding the avrage we need to find the sum of the all numbers 
#the the formula of calculating the arage addition of all num /total number
num=int(input("Enter the Number"))
sum=0
for i in range(1,num+1):
    sum=sum+i
avg=sum/num
print(avg)
