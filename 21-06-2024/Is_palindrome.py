str = input("enter the String :")


def is_palindrome(str):
    return  str[::-1]

revstr = is_palindrome(str)

if revstr == str:
    print("Is Palindrome")
else:
    print("Is Not Palindrome")



