age = int (input("Enter your age: ")) 
if(age>18):
    print("You can drive")
    print("THANK YOU!")
elif(age == 18):
    print("Lets schedule an interview")
elif(age == 0):
    print("Hey you just born")
else:
    print("You can not drive")
    print("SORRY!")