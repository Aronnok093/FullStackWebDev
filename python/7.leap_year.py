year = int(input("Enter a year: "))

if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print("It's a leap year")
else:
    print("It's not a leap year")


#Logics,
#If a year is divisible by 4, it’s a potential leap year.
#If a year is divisible by 100, it’s not a leap year unless 
#it’s also divisible by 400.
