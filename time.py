# Ask user for current time and wait time
currentTimeStr = input("What is the current time (in hours 0-23)? ")
waitTimeStr = input("How many hours do you want to wait? ")

# Convert string input to integers
currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

# Calculate future time (wrap around if it goes over 24)
finalTimeInt = (currentTimeInt + waitTimeInt) % 24

# Print result
print("The time after waiting will be:", finalTimeInt)