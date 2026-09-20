num=int(input("Enter The Number"))
count=0
for i in range(1,num+1):
    if num % i == 0:
        count=count+1
if count==2:
    print(num,"The Given Number Is Prime Number")
else:
    print(num,"The Give Number Is Not Prime Number")