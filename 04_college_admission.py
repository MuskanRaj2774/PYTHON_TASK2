marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 70:
    if age >= 17:
        print("Eligible for admission")
    else:
        print("Age requirement not met")
else:
    print("Marks too low")