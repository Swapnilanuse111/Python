time=int(input("Enter the Current timeing"))
if 5 <= time < 12:
    print("Good Morning")
elif 12 <= time < 17:
    print("Good Afternoon")
elif 17 <= time < 21:
    print("Good Evening")
else:
    print("Good Night")