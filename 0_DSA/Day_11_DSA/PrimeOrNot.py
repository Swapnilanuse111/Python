num=int(input("Enter The String"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("The Number Is Prime")
else:
    print("The Number Is Not Prime")
