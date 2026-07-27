def Fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    # return fact
    print(fact)
a=Fact(5)
print(a)