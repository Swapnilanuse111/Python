num=int(input("Enter The Number:-"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("The Number Is Prime Number")
else:
    print("The Number Not Prime")