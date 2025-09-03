# A time traveler has suddenly appeared in your classroom!

# Ask for the traveler's year of origin
year = int(input("Greetings! What is your year of origin? "))

# Check which time period they are from and respond accordingly
if year <= 1900:
    print("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")