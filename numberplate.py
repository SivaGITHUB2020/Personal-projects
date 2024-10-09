# Create a data base of number plates
np = ["asd123", "qwe147", "cvb369", "sdf159"]

# Enter new number plate
newnp = input("Enter the number plate: ")

# check if new number plate is in the database if not print Red
if newnp in np:
    print("Green, All good!")
else:
    print("Red, No parking permit!")
