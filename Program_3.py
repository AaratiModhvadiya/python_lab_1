def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

# Taking input marks from user
print("Enter marks out of 100 for each subject:")
subject1 = float(input("Subject 1: "))
subject2 = float(input("Subject 2: "))
subject3 = float(input("Subject 3: "))
subject4 = float(input("Subject 4: "))
subject5 = float(input("Subject 5: "))

# Calculating total marks
total_marks = subject1 + subject2 + subject3 + subject4 + subject5

# Calculating average marks
average_marks = total_marks / 5

# Determining grade
grade = calculate_grade(average_marks)

# Displaying the marksheet
print("\n********** Marksheet **********")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Subject 4: {subject4}")
print(f"Subject 5: {subject5}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Grade: {grade}")
