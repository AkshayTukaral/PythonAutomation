# Triangle classifier Program
Side_1 = int(input("Enter the First side of triangle"))
Side_2 = int(input('Enter the Second side of triangle'))
Side_3 = int(input('Enter the Third side of triangle'))

if (Side_1 == Side_2 == Side_3):
    print("This is an Equilateral Triangle")
elif (Side_1 == Side_2) or (Side_3 == Side_2) or (Side_1 == Side_3):
    print("This is an Isosceles Triangle")
elif (Side_1 != Side_2 != Side_3):
    print("This is an Scalene Traingle")
else:
    print("Invalid Input")
