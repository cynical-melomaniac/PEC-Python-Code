year = int(input("Enter Year: "))

if (year % 4 == 0) and (year % 100 != 0):
    print("The year is a leap year.")

elif (year % 100 == 0) and (year % 400 == 0):
    print("The year is a leap year.")

else:
    print("The year is a not leap year.")