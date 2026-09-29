num=int(input("Enter The Number"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("The Given Number Is Prime Number")
else:
    print("The Given Number Is Not Prime Number Becous The DIvisbile Of That Perticular Number Is More Than Two")