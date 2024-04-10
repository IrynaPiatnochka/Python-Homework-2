#Determine if the given year is a leap year

year = int(input("Enter a year: "))

if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0): 
    print('This is a leap year.') 
else: 
    print('This is not a leap year.') 
