#create a function that return true if year is a leap year and false if it was not a leap year

year =  int(input("Enter year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print(True)

elif (year % 4 ==0) and (year % 100 != 0):
    print(True)

else:
    print(False)