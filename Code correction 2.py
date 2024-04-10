#Deciding on the size of the venue based on amount of attendees

attendees = int(input("Enter number of attendees: "))
print("large hall" if attendees > 100 else "conference room")

#Catering Choices

food = input("Would you like vegetarian food? ")
if food == 'yes':
    print("I reccomend 'Veggie Delight Caterers.'")
else:
   print("I reccomend 'Gourmet Meals Caterers.'")
