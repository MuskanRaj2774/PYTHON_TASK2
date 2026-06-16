experience = int(input("Enter years of experience: "))
performance = input("Enter performance (good/bad): ")

if experience >= 2:
    if performance == "good":
        print("Bonus Approved")
    else:
        print("Performance not eligible")
else:
    print("Experience too low")