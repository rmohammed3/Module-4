# Grading Program: Averages 3 exam scores and returns letter grade + pass/fail

# Get inputs
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

# Create a list of grades
grades = [exam_one, exam_two, exam_three]

# Calculate the average
sum_grades = 0
for grade in grades:
    sum_grades += grade

avg = sum_grades / len(grades)

# Determine letter grade
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print results
for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))
print("Grade: " + letter_grade)

# Passing/failing message
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")