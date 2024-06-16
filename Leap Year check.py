Year = int(input("Enter the Year"))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 100):
    print("You have entered a Leap Year")
else:
    print("You have entered a non-Leap year")

