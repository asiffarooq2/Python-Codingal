# Exam Eligibility Test

total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

attendance_percentage = (attended_classes / total_classes) * 100

print("Attendance Percentage =", attendance_percentage, "%")

if attendance_percentage >= 75:
    print("You are eligible to sit for the exam.")
else:
    print("You are not eligible to sit for the exam.")
