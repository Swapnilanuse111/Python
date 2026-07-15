num=int(input("Enter The Number"))
rev=0   #for store the rev number we create a varible rev and value is assignd for that var is 0
while num!=0:
    LastDigit=num%10
    rev=rev*10+LastDigit
    # num=num//10
print(rev)

#secoend approch to print rerse the num and str

