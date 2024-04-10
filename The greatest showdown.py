#2 - The greatest showdown
# Identify the largest number and print it

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b and a>c:
    print('The largest number is ', a)
elif b>c and b>c:
    print('The largest number is ', b)
else:
    print('The largest number is ', c)


#Identify the smallest number and print it

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a<b and a<c:
    print('The smallest number is ', a)
elif b<c and b<c:
    print('The smallest number is ', b)
else:
    print('The smallest number is ', c)