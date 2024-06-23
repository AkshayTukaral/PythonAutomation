str = input("Enter The String: ")

vowels = 0
consonent = 0

for char in str:
    if char in "aeiouAEIOU":
        vowels += 1
    else:
        str.isalpha()
        consonent += 1

print("Vowels :", vowels)
print("Consonents :", consonent)
