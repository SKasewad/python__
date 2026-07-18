str1 = input("Enter first string:")
str2 = input("Enter sec string:")
if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagram")
else:
    print("Not Allowed")
    