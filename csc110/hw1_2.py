
homework = float(input("Enter Homework grade: "))
midterm = float(input("Enter Midterm grade: "))
final = float(input("Enter Final Exam grade: "))

finalGrade = ((homework * .45) + (midterm * .25) + (final * .3))

print("Your final grade is: ", round(finalGrade, 2))
