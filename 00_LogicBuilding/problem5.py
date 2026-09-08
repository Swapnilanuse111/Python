year=int(input("Eneter The Year"))
if year%400==0:
    print("This Is Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("This Is Leap Year")
else:
    print("This Is not leap year")