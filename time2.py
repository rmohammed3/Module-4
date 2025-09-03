# Ask user for current time and hours to wait
str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")

# Convert to integers
time = int(str_time)
wait_time = int(str_wait_time)

# Calculate alarm time (wrap around 24-hour format)
time_when_alarm_go_off = (time + wait_time) % 24

# Print result
print("The alarm will go off at:", time_when_alarm_go_off)