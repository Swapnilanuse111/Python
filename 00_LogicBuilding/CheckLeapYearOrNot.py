year=int(input("Enter the Year"))
if year%400==0:
    print("The Year is Leap")
elif year%100==0:
    print("This year is not leap year")
elif year%4==0:
    print("This Year Is leap year")
else:
    print("This Is not leap year")
